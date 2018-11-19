"""For the PHYSICAL robot, tentative results.
"""
import argparse, copy, cv2, json, os, sys, pickle
import time, datetime, logging
import numpy as np
from os.path import join
from collections import defaultdict
import torch
from torchvision import transforms

import rospy, hsrb_interface
from hsrb_interface import geometry
from hsr_core.sensors import RGBD
from hsr_core.rgbd_to_map import RGBD2Map  # creates rgbd frame for camera pix -> world space
from hsr_core.utils import process_depth
from il_ros_hsr.nets.net import ActPredictorNet
from il_ros_hsr.nets import options as opt
from il_ros_hsr.nets import custom_transforms as CT

# Ideally remove this later
from il_ros_hsr.core.grasp_planner import GraspPlanner
from il_ros_hsr.p_pi.bed_making.gripper import Bed_Gripper


def _save_and_viz(pth_t, pth_tp1, img_t, img_tp1, out_pos, out_ang):
    """Really need to put much of this in `options.py` and reuse among scripts.
    """
    out_pos = out_pos.cpu().detach().numpy().squeeze()
    if not os.path.exists(opt.DEPLOY_TMPDIR):
        os.makedirs(opt.DEPLOY_TMPDIR)
    b_pth_t   = os.path.basename(pth_t)
    b_pth_tp1 = os.path.basename(pth_tp1)
    print("base pth_t:   {}".format(b_pth_t))
    print("base pth_tp1: {}".format(b_pth_tp1))
    print("predicted position:     {}".format(out_pos))
    print("predicted angle logits: {}".format(out_ang))

    # The raw images
    hstack1 = np.concatenate((img_t, img_tp1), axis=1)
    fname1 = join(opt.DEPLOY_TMPDIR,'{}_1.png'.format(b_pth_t))
    cv2.imwrite(fname1, hstack1)
    print("Look at: {}".format(fname1))

    # Transformed images, but _without_ the tensor and normalization stuff.
    transforms_valid_notensors = transforms.Compose([
        CT.Rescale((256,256)),
        CT.CenterCrop((224,224)),
    ])
    t_input = transform_imgs(img_t, img_tp1, transforms_valid_notensors)
    t_img_t   = t_input['img_t']
    t_img_tp1 = t_input['img_tp1']
    h, w, c = t_img_t.shape

    # Save the _transformed_ images.
    hstack2 = np.concatenate((t_img_t, t_img_tp1), axis=1)
    fname2 = join(opt.DEPLOY_TMPDIR,'{}_2.png'.format(b_pth_t))
    cv2.imwrite(fname2, hstack2)
    print("Look at: {}".format(fname2))

    # Overlay some stuff on the images (must de-process label, though).
    pred_pos_int = int(out_pos[0]*w), int(out_pos[1]*h)
    img = np.ascontiguousarray(t_img_t, dtype=np.uint8)
    cv2.circle(img, center=pred_pos_int, radius=2, color=opt.BLUE,  thickness=-1)
    cv2.circle(img, center=pred_pos_int, radius=3, color=opt.GREEN, thickness=1)
    cv2.putText(img=img, 
                text="pred pos: {}".format(pred_pos_int),
                org=(10,15),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                fontScale=0.5, 
                color=opt.GREEN,
                thickness=1)

    # Save _transformed_ images, WITH predicted stuff overlaid on it.
    hstack3 = np.concatenate((img, t_img_tp1), axis=1)
    fname3 = join(opt.DEPLOY_TMPDIR,'{}_3.png'.format(b_pth_t))
    cv2.imwrite(fname3, hstack3)
    print("Look at: {}".format(fname3))
    print("PS, t_img_t.shape: {}".format(t_img_t.shape))


def transform_imgs(img_t, img_tp1, transform):
    """Designed for test-time inference.
    
    During training and validation, we have a class which works by taking pickle
    file with lists of the data in training / validation, and it processes them.
    But here, we assume we want to pass a new image to the model. The issue,
    however, is that the transforms that we use for validation (which we should
    use for test-time inference on new images with no labels) rely on assuming
    we have a target. So we will just add fictional targets.

    Parameters
    ----------
    img_t, img_tp1:
        Two numpy arrays representing the two images for the network. We return
        their transformations.
    transform:
        Set of composed transforms that we used for VALIDATION.
    """
    assert img_t.shape == img_tp1.shape

    # Fictional targets so that we can apply the same validation set transforms
    # Another way is to set transform classes to optionally ignore targets?
    target_xy  = [0.0, 0.0]
    target_l   = [0.0]
    target_ang = [1.0, 0.0, 0.0, 0.0]

    # Feed through our transformations and return.
    sample = {
        'img_t':      img_t,
        'img_tp1':    img_tp1, 
        'target_xy':  target_xy,
        'target_l':   target_l,
        'target_ang': target_ang,
        'raw_ang':    -1,
    }
    sample = transform(sample)
    return sample


# Will put in `options.py` later
TARGET_DIR = 'tmp_physical_targs'


class DataCollector:

    def __init__(self, args):
        self.args = args
        self.robot = robot = hsrb_interface.Robot()
        self.omni_base = robot.get('omni_base')
        self.whole_body = robot.get('whole_body')
        self.cam = RGBD()
        self.data = dict() # list of processed depth images and actions taken (I_t, a_t)

        # We don't use directly, but it makes a frame that we need for pixels -> world grasp poses.
        self.rgbd_map = RGBD2Map() # makes frame we need but we don't use it otherwise

        # TODO: eventually we need to remove this. Doing this to let us go from
        # camera coordinates to world frame, but we need HSR_CORE to support it.
        # But, should be easy because the grasp planner is pretty simple and we
        # only use it to compute the average depth values in a region.
        self.gp = GraspPlanner()
        self.gripper = Bed_Gripper(self.gp, self.cam, options=None, gripper=robot.get('gripper'))

        # Also this is a bit hacky. We want the HSR to rotate so that it's
        # _facing_ the bed now, whereas it started facing 'sideways'. Makes a
        # target pose for the robot so it goes there, before grasp executiuon.
        # TODO: make pose here. I think we can get away with rotating wrt the
        # map but in general we want to create our own poses.

        print("Initialized the data collector! Resting for 2 seconds...")
        time.sleep(2)

        # Hande the part about loading the network and pretrained model.
        HEAD  = '/nfs/diskstation/seita/bedmake_ssl'
        MODEL = 'resnet18_2018-11-18-09-50_000'
        PATH  = join(HEAD, MODEL, 'act_predictor.pt')

        # Get old args we used, and put into a newer Namespace object.
        with open(join(HEAD, MODEL, 'args.json'), 'r') as fh:
            saved_args = json.load(fh)
        self.netargs = opt._json_to_args(jsonfile=saved_args)
        
        # Load the pretrained model.
        model = opt.get_pretrained_model(self.netargs)
        self.act_predictor = ActPredictorNet(model, self.netargs)
        self.act_predictor.load_state_dict(torch.load(PATH))
        self.act_predictor.eval()

        self.transforms_valid = transforms.Compose([
            CT.Rescale((256,256)),
            CT.CenterCrop((224,224)),
            CT.ToTensor(),
            CT.Normalize(opt.MEAN, opt.STD),
        ])


    def orient_robot(self):
        """Orients the robot so that it is in a good position to take pictures.
        Make sure the HSR is starting about a foot away from the long side of the bed, 
        facing parallel to the bed towards the top.
        """
        self.whole_body.move_to_go()
        self.whole_body.move_to_joint_positions({'arm_flex_joint':  -np.pi/16.0})
        self.whole_body.move_to_joint_positions({'head_pan_joint':   np.pi/2.0})
        self.whole_body.move_to_joint_positions({'head_tilt_joint': -np.pi/4.0})
        self.whole_body.move_to_joint_positions({'arm_lift_joint':   0.120})
    

    def get_images(self):
        c_img = self.cam.read_color_data()
        d_img = self.cam.read_depth_data()
        d_img_proc = process_depth(d_img)
        return (c_img, d_img, d_img_proc)


    def get_target_images(self):
        """Get a series of target images, stopping only when user wishes to
        abort (via pressing ESC key).

        Note, in this phase, we add onto existing indices in saved target dir.
        We assume we can sort these, then extract the index from the last item.
        """
        args = self.args
        if not os.path.exists(TARGET_DIR):
            os.makedirs(TARGET_DIR)
        digits = 3

        # Get the index we should start with for saving imgs.
        saved_imgs = sorted([x for x in os.listdir(TARGET_DIR)])
        if len(saved_imgs) == 0:
            idx = 0
        else:
            saved_img_noext = (saved_imgs[0]).replace('.png','')
            idx = int( (saved_img_noext.split('_'))[-1] )

        while True:
            c_img, d_img, d_img_proc = self.get_images()

            if (c_img.all() is not None) and (d_img.all() is not None):
                # Once we get here, we've saved the images. BUT, since the code
                # stops here, we should change the bed making setup. THEN we
                # press any key. This way, next time step has the new images.
                caption = 'Here is data (ESC to abort). NOTE: CHANGE THE IMAGE for next time step'
                opt.call_wait_key( cv2.imshow(caption, d_img_proc) )

                sidx = str(idx).zfill(digits)
                pth1 = join(TARGET_DIR, 'c_img_{}.png'.format(sidx))
                pth2 = join(TARGET_DIR, 'd_img_{}.png'.format(sidx))
                pth3 = join(TARGET_DIR, 'd_img_proc_{}.png'.format(sidx))
                cv2.imwrite(pth1, c_img)
                cv2.imwrite(pth2, d_img)
                cv2.imwrite(pth3, d_img_proc)
                print("Saved:")
                print("  {}".format(pth1))
                print("  {}".format(pth2))
                print("  {}".format(pth3))
                idx += 1


    def deploy(self):
        """Deploy!!
        
        Careful, did you run the first phases beforehand to check that (a) there
        exist target images you can use, and (b) that the poses in rviz look
        reasonable.
        """        
        idx = 0

        # Pick images to try from the saved file, and then current image.
        pth_end = 'tmp_physical_targs/d_img_proc_000.png'
        img_end = cv2.imread(pth_end)
        c_img, d_img, d_img_proc = self.get_images()
        assert c_img.shape == d_img_proc.shape == (480,640,3), c_img.shape
        assert d_img.shape == (480,640), d_img.shape

        # Visualize current and target image initially.
        caption1 = 'Full size images. ESC to abort, other key to proceed.'
        img_t = d_img_proc
        hstack1 = np.concatenate((img_t, img_end), axis=1)
        opt.call_wait_key( cv2.imshow(caption1, hstack1) )

        # Next, network predictions.
        t_input   = transform_imgs(img_t, img_end, self.transforms_valid)
        t_img_t   = t_input['img_t'].unsqueeze(0)    # after unsqueezes, both
        t_img_end = t_input['img_tp1'].unsqueeze(0)  # w/shape: (1,3,224,224)
        out_pos, out_ang = self.act_predictor(t_img_t, t_img_end)
        assert t_img_t.shape == t_img_end.shape == (1,3,224,224)
        out_pos = out_pos.cpu().detach().squeeze()
        out_ang = out_ang.cpu().detach().squeeze()

        # Post-process to visualize for humans. See `deploy_test` for some
        # earlier tests I did. We should eventually make it less dependent on
        # hard-coded values, but only if we're changing the transforms.
        w, h = 224, 224
        pred_pos_proc = int(out_pos[0]*w), int(out_pos[1]*h)

        # Get predicted position w.r.t. the original (480,640)-sized image.
        pred_pos = (pred_pos_proc[0] + 16, pred_pos_proc[1] + 16)
        widthf  = 640.0 / 256.0
        heightf = 480.0 / 256.0
        pred_pos = ( int(pred_pos[0]*widthf), int(pred_pos[1]*heightf) )

        # Show and visualize to the user.
        caption2 = 'Predicted Pos on full image: {}'.format(pred_pos)
        img = np.copy(img_t)
        assert img.shape == (480,640,3), img.shape
        cv2.circle(img, center=pred_pos, radius=4, color=opt.BLUE,  thickness=-1)
        cv2.circle(img, center=pred_pos, radius=6, color=opt.GREEN, thickness=1)
        hstack2 = np.concatenate((img, img_end), axis=1)
        opt.call_wait_key( cv2.imshow(caption2, hstack2) )

        # Some debugging/logging.
        print("pred_pos for 224x224 img: {} (scaled {})".format(out_pos, pred_pos_proc))
        print("pred_pos for 480x640 img: {}".format(pred_pos))
        print("out angle (logits): {}".format(out_ang))
        print("current idx for grasp pose: {}".format(idx))
        # TODO: later, save in a principled manner.

        # Broadcast the target grasp onto world space. See `main/deploy.py` for details.
        self.gripper.find_pick_region_net(pred_pos, c_img, d_img, idx, 'BOTTOM')
        print("We have now broadcasted the bed_0 and bed_i_0 poses !!! Now execute grasp")
        time.sleep(1)

        # Rotate the robot 90 degrees so it now faces the bed, w.r.t. the map frame.
        self.omni_base.move(geometry.pose(ek=1.57), 500.0, ref_frame_id='map')

        # TODO: execute the grasp, after rotating. See `main/deploy.py` for details.
        # I think we can borrow this segment from `p_pi/bed_making/gripper.py`

        ## whole_body.end_effector_frame = 'hand_palm_link'

        ## # Hmmm ... might help with frequent table bumping? Higher = more arm movement.
        ## whole_body.linear_weight = 60.0

        ## whole_body.move_end_effector_pose(geometry.pose(),cards[0])
        ## self.com.grip_squeeze(self.gripper)

        ## # Then after we grip, go back to the default value.
        ## whole_body.linear_weight = 3.0

        ## # Then we pull.
        ## self.tension.force_pull(whole_body,direction)
        ## self.com.grip_open(self.gripper)

        # And then optionally repeat the process and save ... that's trivial.
        # TODO


if __name__ == "__main__":
    # --------------------------------------------------------------------------
    pp = argparse.ArgumentParser()
    pp.add_argument('--phase', type=int, help='see code and README docs')
    args = pp.parse_args()
    assert args.phase in [0,1,2]
    # --------------------------------------------------------------------------

    dc = DataCollector(args)
    dc.orient_robot()

    if args.phase == 0:
        # First, focus on getting a set of target images for the robot. Easy to
        # do it here because we assume that once we're done the robot is in the
        # same position for the next phase (trying to grasp and pull) so we do
        # not have to worry about position and orientation issues.
        dc.get_target_images()
    elif args.phase == 1:
        # Ensure that the poses look good. Start up rviz and look at the map
        # pose. Ideally we have a better way of doing this, though ... this
        # serves the same purpose as phase 1 in my earlier code.
        print("Look at rviz and check that poses are good.")
        print("E.g., robot base should be facing in positive x-axis direction")
        print("which should be aligned with the long edge of the bed.")
        rospy.spin()
    elif args.phase == 2:
        dc.deploy()
    else:
        raise NotImplementedError()
