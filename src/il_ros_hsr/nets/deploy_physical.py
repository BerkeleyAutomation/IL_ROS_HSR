"""For the PHYSICAL robot, tentative results.
"""
import torch
import argparse, copy, cv2, json, os, sys, time, pickle
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


    ##def collect_data(self, ep, ts): ##    """Does one instance of data collection, then saves. ep=episode, ts=time_step.
    ##    """
    ##    (c_img, d_img, d_img_proc) = self.get_images()
    ##    pth1 = join(TARGET_DIR, 'c_img_{}_{}.png'.format(str(ep).zfill(2), str(ts).zfill(3)))
    ##    pth2 = join(TARGET_DIR, 'd_img_{}_{}.png'.format(str(ep).zfill(2), str(ts).zfill(3)))
    ##    pth3 = join(TARGET_DIR, 'd_img_proc_{}_{}.png'.format(str(ep).zfill(2), str(ts).zfill(3))) ##    self.data[(ep, ts)] = {"image": d_img_proc, "action": None} ##    cv2.imwrite(pth1, c_img)
    ##    cv2.imwrite(pth2, d_img)
    ##    cv2.imwrite(pth3, d_img_proc)


    ##def record_action(self, action, episode, time_step): 
    ##    """Saves a_t, the action vector at time t = self.idx: [grasp_x, grasp_y, angle, length]
    ##    """
    ##    self.data[(episode, time_step)]["action"] = \
    ##            {'x': action[0], 'y': action[1], 'angle': action[2], 'length': action[3]}


    ##def pickle(self):
    ##    with open(os.path.join(TARGET_DIR, 'rollout2.pkl'), 'wb') as handle:
    ##        pickle.dump(self.data, handle, protocol=pickle.HIGHEST_PROTOCOL)


    ##def display_episode(self, image, episode_num):
    ##    """Shows an image between data collection episodes notifying the user to reset the blanket.
    ##    """
    ##    cv2.imshow("EPISODE {} STARTING. Please reset blanket position, then press any key.".format(str(episode_num)), image)
    ##    cv2.waitKey()
    ##    cv2.destroyAllWindows()


    ##def compute_grasps(self):
    ##    self.data = pickle.load(open('/nfs/diskstation/ryanhoque/ssldata/rollout.pkl', 'rb'))
    ##    for k in self.data:
    ##        image = cv2.imread('/nfs/diskstation/ryanhoque/ssldata/c_img_{}_{}.png'.format(
    ##                str(k[0]).zfill(2), str(k[1]).zfill(3)))
    ##        cv2.imshow("", image)
    ##        cv2.waitKey()
    ##        cv2.destroyAllWindows()
    ##        try:
    ##            x, y = red_contour(image)
    ##        except: # cannot find red contour, so enter it manually
    ##            cv2.imshow("", image)
    ##            cv2.waitKey()
    ##            cv2.destroyAllWindows()
    ##            print("error: cannot find contour")
    ##            x = int(raw_input("enter x pixel\n"))
    ##            y = int(raw_input("enter y pixel\n"))
    ##        if self.data[k]["action"]:
    ##            self.data[k]["action"]['x'] = x
    ##            self.data[k]["action"]['y'] = y


    def get_target_images(self):
        """Runs the pipeline for deployment, testing out bed-making.
        """
        # Get the starting image (from USB webcam). Try a second as well.
        cap = cv2.VideoCapture(0)
        frame = None
        while frame is None:
            ret, frame = cap.read()
            cv2.waitKey(50)
        self.image_start = frame
        cv2.imwrite('image_start.png', self.image_start)

        _, frame = cap.read()
        self.image_start2 = frame
        cv2.imwrite('image_start2.png', self.image_start2)

        cap.release()
        print("NOTE! Recorded `image_start` for coverage evaluation. Was it set up?")

        def get_pose(data_all):
            # See `find_pick_region_labeler` in `p_pi/bed_making/gripper.py`.
            # It's because from the web labeler, we get a bunch of objects.
            # So we have to compute the pose (x,y) from it.
            res = data_all['objects'][0]
            x_min = float(res['box'][0])
            y_min = float(res['box'][1])
            x_max = float(res['box'][2])
            y_max = float(res['box'][3])
            x = (x_max - x_min)/2.0 + x_min
            y = (y_max - y_min)/2.0 + y_min
            return (x,y)

        args = self.args
        use_d = BED_CFG.GRASP_CONFIG.USE_DEPTH
        self.get_new_grasp = True
        self.new_grasp = True
        self.rollout_stats = [] # What we actually save for analysis later

        # Add to self.rollout_stats at the end for more timing info
        self.g_time_stats = []      # for _execution_ of a grasp
        self.move_time_stats = []   # for moving to the other side

        while True:
            c_img = self.cam.read_color_data()
            d_img = self.cam.read_depth_data()

            if (not c_img.all() == None and not d_img.all() == None):
                if self.new_grasp:
                    self.position_head()
                else:
                    self.new_grasp = True
                time.sleep(3)

                c_img = self.cam.read_color_data()
                d_img = self.cam.read_depth_data()
                d_img_raw = np.copy(d_img) # Needed for determining grasp pose

                # --------------------------------------------------------------
                # Process depth images! Helps network, human, and (presumably) analytic.
                # Obviously human can see the c_img as well ... hard to compare fairly.
                # --------------------------------------------------------------
                if use_d:
                    if np.isnan(np.sum(d_img)):
                        cv2.patchNaNs(d_img, 0.0)
                    d_img = depth_to_net_dim(d_img, robot='HSR')
                    policy_input = np.copy(d_img)
                else:
                    policy_input = np.copy(c_img)

                # --------------------------------------------------------------
                # Run grasp detector to get data=(x,y) point for target, record stats.
                # Note that the web labeler returns a dictionary like this:
                # {'objects': [{'box': (155, 187, 165, 194), 'class': 0}], 'num_labels': 1}
                # but we really want just the 2D grasping point. So use `get_pose()`.
                # Also, for the analytic one, we'll pick the highest point ourselves.
                # --------------------------------------------------------------
                sgraspt = time.time()
                if args.g_type == 'network':
                    data = self.g_detector.predict(policy_input)
                elif args.g_type == 'analytic':
                    data_all = self.wl.label_image(policy_input)
                    data = get_pose(data_all)
                elif args.g_type == 'human':
                    data_all = self.wl.label_image(policy_input)
                    data = get_pose(data_all)
                egraspt = time.time()

                g_predict_t = egraspt - sgraspt
                print("Grasp predict time: {:.2f}".format(g_predict_t))
                self.record_stats(c_img, d_img_raw, data, self.side, g_predict_t, 'grasp')

                # For safety, we can check image and abort as needed before execution.
                if use_d:
                    img = self.dp.draw_prediction(d_img, data)
                else:
                    img = self.dp.draw_prediction(c_img, data)
                caption = 'G Predicted: {} (ESC to abort, other key to proceed)'.format(data)
                call_wait_key( cv2.imshow(caption,img) )

                # --------------------------------------------------------------
                # Broadcast grasp pose, execute the grasp, check for success.
                # We'll use the `find_pick_region_net` since the `data` is the
                # (x,y) pose, and not `find_pick_region_labeler`.
                # --------------------------------------------------------------
                self.gripper.find_pick_region_net(pose=data,
                                                  c_img=c_img,
                                                  d_img=d_img_raw,
                                                  count=self.grasp_count,
                                                  side=self.side,
                                                  apply_offset=self.apply_offset)
                pick_found, bed_pick = self.check_card_found()

                if self.side == "BOTTOM":
                    self.whole_body.move_to_go()
                    self.tt.move_to_pose(self.omni_base,'lower_start')
                    tic = time.time()
                    self.gripper.execute_grasp(bed_pick, self.whole_body, 'head_down')
                    toc = time.time()
                else:
                    self.whole_body.move_to_go()
                    self.tt.move_to_pose(self.omni_base,'top_mid')
                    tic = time.time()
                    self.gripper.execute_grasp(bed_pick, self.whole_body, 'head_up')
                    toc = time.time()
                self.g_time_stats.append( toc-tic )
                self.check_success_state(policy_input)


if __name__ == "__main__":
    # --------------------------------------------------------------------------
    pp = argparse.ArgumentParser()
    pp.add_argument('--phase', type=int, help='1 for checking images/poses, 2 for deployment.')
    ##pp.add_argument('--g_type', type=str, help='must be in [network, human, analytic]')
    ##pp.add_argument('--use_rgb', action='store_true', default=False,
    ##    help='If doing this, we need to use the rgb network.')
    args = pp.parse_args()
    assert args.phase in [1,2]
    # --------------------------------------------------------------------------

    dc = DataCollector(args)
    dc.orient_robot()

    if args.phase == 1:
        # First, focus on getting a set of target images for the robot.
        dc.get_target_images()
    else:
        raise NotImplementedError()
