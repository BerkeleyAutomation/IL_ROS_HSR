"""For the PHYSICAL robot, tentative results.
"""
import torch
import argparse, copy, cv2, json, os, sys, time, pickle, logging
import time, datetime
import numpy as np
from os.path import join
from collections import defaultdict

import hsrb_interface
from hsr_core.sensors import RGBD
from hsr_core.utils import process_depth
from il_ros_hsr.nets.net import ActPredictorNet
from il_ros_hsr.nets import options as opt
from il_ros_hsr.nets import custom_transforms as CT


###def transform_imgs(img_t, img_tp1, transform):
###    """Designed for test-time inference.
###    
###    During training and validation, we have a class which works by taking pickle
###    file with lists of the data in training / validation, and it processes them.
###    But here, we assume we want to pass a new image to the model. The issue,
###    however, is that the transforms that we use for validation (which we should
###    use for test-time inference on new images with no labels) rely on assuming
###    we have a target. So we will just add fictional targets.
###
###    Parameters
###    ----------
###    img_t, img_tp1:
###        Two numpy arrays representing the two images for the network. We return
###        their transformations.
###    transform:
###        Set of composed transforms that we used for VALIDATION.
###    """
###    assert img_t.shape == img_tp1.shape
###
###    # Fictional targets so that we can apply the same validation set transforms
###    # Another way is to set transform classes to optionally ignore targets?
###    target_xy  = [0.0, 0.0]
###    target_l   = [0.0]
###    target_ang = [1.0, 0.0, 0.0, 0.0]
###
###    # Feed through our transformations and return.
###    sample = {
###        'img_t':      img_t,
###        'img_tp1':    img_tp1, 
###        'target_xy':  target_xy,
###        'target_l':   target_l,
###        'target_ang': target_ang,
###        'raw_ang':    -1,
###    }
###    sample = transform(sample)
###    return sample
###
###
###def deploy(act_predictor):
###    """Let's see how to load just directly from two png images.
###    
###    In theory we should figure out what we can avoid from all the data loading
###    machinery when we trained this network.
###    """
###    transforms_valid = transforms.Compose([
###        CT.Rescale((256,256)),
###        CT.CenterCrop((224,224)),
###        CT.ToTensor(),
###        CT.Normalize(opt.MEAN, opt.STD),
###    ])
###
###    # Pick images to try here; careful, don't pick 'boundaries' of episodes.
###    pth_t   = 'ssldata2/d_img_proc_10_003.png'
###    pth_tp1 = 'ssldata2/d_img_proc_10_004.png'
###    img_t   = cv2.imread(pth_t)
###    img_tp1 = cv2.imread(pth_tp1)
###
###    t_input    = transform_imgs(img_t, img_tp1, transforms_valid)
###    t_imgs_t   = t_input['img_t'].unsqueeze(0)
###    t_imgs_tp1 = t_input['img_tp1'].unsqueeze(0)
###
###    out_pos, out_ang = act_predictor(t_imgs_t, t_imgs_tp1)
###    _save_and_viz(pth_t, pth_tp1, img_t, img_tp1, out_pos, out_ang)
###
###
###if __name__ == "__main__":
###    # Pick the model that we want to load.
###    HEAD  = '/nfs/diskstation/seita/bedmake_ssl'
###    MODEL = 'resnet18_2018-11-18-09-50_000'
###    PATH  = join(HEAD, MODEL, 'act_predictor.pt')
###
###    # Get old args we used, and put into a newer Namespace object.
###    with open(join(HEAD, MODEL, 'args.json'), 'r') as fh:
###        saved_args = json.load(fh)
###    args = opt._json_to_args(jsonfile=saved_args)
###
###    # Load the pretrained model. If you print state dict, these start with
###    # `layer` as that was the convention with the ResNet saved models.
###    model = opt.get_pretrained_model(args)
###
###    # But now we use act predictor, with `pretrained_stem` in state dict.
###    act_predictor = ActPredictorNet(model, args)
###    #opt.debug_state_dict(model=act_predictor)
###    act_predictor.load_state_dict(torch.load(PATH))
###    act_predictor.eval()
###
###    deploy(act_predictor)






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
        print("Initialized the data collector! Resting for 2 seconds...")
        time.sleep(2)


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

        Note, in phase 1, we will just add onto existing indices in saved target
        dir. We assume that we can sort these, then extract the index from the
        last element.
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


if __name__ == "__main__":
    # --------------------------------------------------------------------------
    pp = argparse.ArgumentParser()
    pp.add_argument('--phase', type=int, help='see code and README docs')
    args = pp.parse_args()
    assert args.phase in [1,2]
    # --------------------------------------------------------------------------

    dc = DataCollector(args)
    dc.orient_robot()

    if args.phase == 1:
        # First, focus on getting a set of target images for the robot. Easy to
        # do it here because we assume that once we're done the robot is in the
        # same position for the next phase (trying to grasp and pull) so we do
        # not have to worry about position and orientation issues.
        dc.get_target_images()
    else:
        raise NotImplementedError()
