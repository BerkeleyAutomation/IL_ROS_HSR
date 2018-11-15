"""
Collect data fast: the human chooses the direction, and a program finds the grasp points afterwards.
(c) 2018 by Daniel Seita, Ryan Hoque
"""
from hsr_core.sensors import RGBD
from hsr_core.utils import process_depth
import cv2, hsrb_interface, os, sys, time, pickle
import numpy as np

USERNAME = 'ryanhoque' # change as needed
TARGET_DIR = '/nfs/diskstation/{}/ssldata'.format(USERNAME)

def red_contour(image):
    """Finds the red contour in a color image. 
    Courtesy of Ron Berenstein, with tiny modifications.
    """
    b, g, r = cv2.split(image)
    bw0 = (r[:,:]>150).astype(np.uint8)*255

    bw1 = cv2.divide(r, g[:, :] + 1)
    bw1 = (bw1[:, :] > 1.5).astype(np.uint8)*255
    bw1 = np.multiply(bw1, bw0).astype(np.uint8) * 255
    bw2 = cv2.divide(r, b[:,:]+1)
    bw2 = (bw2[:, :] > 1.5).astype(np.uint8)*255

    bw = np.multiply(bw1, bw2).astype(np.uint8) * 255
    kernel = np.ones((5, 5), np.uint8)
    bw = cv2.morphologyEx(bw, cv2.MORPH_OPEN, kernel)
    bw = cv2.dilate(bw, kernel, iterations=1)
    _, bw = cv2.threshold(bw,0,255,0)

    # Now get the actual contours.  Note that contour detection requires a
    # single channel image. Also, we only want the max one as that should be
    # where the sewn patch is located.
    (_, cnts, _) = cv2.findContours(bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt_largest = max(cnts, key = lambda cnt: cv2.contourArea(cnt))

    # Find the centroid in _pixel_space_. Draw it.
    try:
        M = cv2.moments(cnt_largest)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        return (cX,cY)
    except:
        print("PROBLEM: CANNOT FIND CORNER ...")

class DataCollector:

    def __init__(self):
        self.robot = robot = hsrb_interface.Robot()
        self.omni_base = robot.get('omni_base')
        self.whole_body = robot.get('whole_body')
        self.cam = RGBD()
        self.data = dict() # list of processed depth images and actions taken (I_t, a_t)
        self.color = dict()
        print("Initialized the data collector! Resting for 2 seconds...")
        time.sleep(2)

    def orient_robot(self):
        """Orients the robot so that it is in a good position to take pictures.
        Make sure the HSR is starting about a foot away from the long side of the bed, 
        facing parallel to the bed towards the top.
        """
        self.whole_body.move_to_go()
        self.whole_body.move_to_joint_positions({'arm_flex_joint': -np.pi/16.0})
        self.whole_body.move_to_joint_positions({'head_pan_joint': np.pi/2.0})
        self.whole_body.move_to_joint_positions({'head_tilt_joint': -np.pi/4.0})
        self.whole_body.move_to_joint_positions({'arm_lift_joint': 0.120})
    
    def get_images(self):
        c_img = self.cam.read_color_data()
        d_img = self.cam.read_depth_data()
        d_img_proc = process_depth(d_img)
        return (c_img, d_img, d_img_proc)


    def collect_data(self, episode, time_step):
        """Does one instance of data collection, then saves.
        """
        (c_img, d_img, d_img_proc) = self.get_images()
        pth1 = os.path.join(TARGET_DIR, 'c_img_{}_{}.png'.format(str(episode).zfill(2), str(time_step).zfill(3)))
        pth2 = os.path.join(TARGET_DIR, 'd_img_{}_{}.png'.format(str(episode).zfill(2), str(time_step).zfill(3)))
        pth3 = os.path.join(TARGET_DIR, 'd_img_proc_{}_{}.png'.format(str(episode).zfill(2), str(time_step).zfill(3)))
        self.data[(episode, time_step)] = {"image": d_img_proc, "action": None}
        self.color[(episode, time_step)] = {"image": c_img}
        cv2.imwrite(pth1, c_img)
        cv2.imwrite(pth2, d_img)
        cv2.imwrite(pth3, d_img_proc)

    def record_action(self, action, episode, time_step): 
        """Saves a_t, the action vector at time t = self.idx: [grasp_x, grasp_y, angle, length]
        """
        self.data[(episode, time_step)]["action"] = {'x': action[0], 'y': action[1], 'angle': action[2], 'length': action[3]}

    def pickle(self):
        with open(os.path.join(TARGET_DIR, 'rollout.pkl'), 'wb') as handle:
            pickle.dump(self.data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def display_episode(self, image, episode_num):
        """Shows an image between data collection episodes notifying the user to reset the blanket.
        """
        cv2.imshow("EPISODE {} STARTING. Please reset blanket position, then press any key.".format(str(episode_num)), image)
        cv2.waitKey()
        cv2.destroyAllWindows()

    def compute_grasps():
        for k in self.color:
            x, y = red_contour(self.color[k])
            if self.data[k]["action"]:
                self.data[k]["action"]['x'] = x
                self.data[k]["action"]['y'] = y


NUM_EPISODES = 10
NUM_ACTIONS_PER_EPISODE = 20

if __name__ == "__main__":
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
    dc = DataCollector()
    dc.orient_robot()
    grasp = ''
    for _episode in range(NUM_EPISODES):
        # (re)set the blanket to a random, not overly complex starting position (e.g. one gentle fold)
        print("Episode " + str(_episode) + "starting!")
        dc.display_episode(dc.get_images()[0], _episode + 1)
        dc.collect_data(_episode + 1, 0) # record time step 0 image (initial state) for this episode
        for _action in range(NUM_ACTIONS_PER_EPISODE):
            grasp = raw_input("Grasp " + str(_action) + "\n")
            action = [None, None, None, 20]
            if grasp == 'w':
                action[2] = 90
            elif grasp == 'a':
                action[2] = 180
            elif grasp == 's':
                action[2] = 0
            elif grasp == 'd':
                action[2] = 270
            elif grasp == 'q':
                break
            dc.record_action(action, _episode + 1, _action)
            # take image I_t+1
            dc.collect_data(_episode + 1, _action + 1)
        if grasp == 'q':
            break
    dc.pickle()
    print("Done with pickling! Computing grasps...")
    # fill in grasps afterwards
    dc.compute_grasps()
    dc.pickle()
    print("Done.")
