"""
Script for collecting images on the HSR for the bed-making project.
(c) 2018 by Daniel Seita, Ryan Hoque
"""
from hsr_core.sensors import RGBD
import cv2, hsrb_interface, os, sys, time, pickle
import numpy as np

USERNAME = 'ryanhoque' # change as needed
TARGET_DIR = '/nfs/diskstation/{}/ssldata'.format(USERNAME)

def process_depth(d_img, thresh=1000):
    """Example of how to process depth images to make them look prettier.
    As an obvious reminder, if you are saving depth images, you should save the
    raw depth images in addition to processed versions.
    Parameters
    ----------
    d_img: (np.array)
        Raw np.array of depth data values.
    thresh: (int)
        Distance threshold for when to 'black out' points, useful for
        simplifying data.
    """
    def depth_to_3ch(img, cutoff):
        """Useful to turn the background into black into the depth images.
        """
        w,h = img.shape
        new_img = np.zeros([w,h,3])
        img = img.flatten()
        img[img>cutoff] = 0.0 
        img = img.reshape([w,h])
        for i in range(3):
            new_img[:,:,i] = img 
        return new_img
    
    
    def depth_scaled_to_255(img):
        """Scale into [0,256), equalize histograms.
        """
        assert np.max(img) > 0.0
        img = 255.0/np.max(img)*img
        img = np.array(img,dtype=np.uint8)
        for i in range(3):
            img[:,:,i] = cv2.equalizeHist(img[:,:,i])
        return img 

    d_img = depth_to_3ch(d_img, thresh)
    d_img = depth_scaled_to_255(d_img)
    return d_img

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
        peri = cv2.arcLength(cnt_largest, True)
        approx = cv2.approxPolyDP(cnt_largest, 0.02*peri, True)
        cv2.circle(image, (cX,cY), 25, (0, 0, 255), 2)
        cv2.line(image, (cX, cY - 35), (cX, cY + 35), (0, 0, 255), 2) # add crosshairs
        cv2.line(image, (cX - 35, cY), (cX + 35, cY), (0, 0, 255), 2)
        return (image,cX,cY)
    except:
        print("PROBLEM: CANNOT FIND CORNER ...")

class DataCollector:

    def __init__(self):
        self.robot = robot = hsrb_interface.Robot()
        self.omni_base = robot.get('omni_base')
        self.whole_body = robot.get('whole_body')
        self.cam = RGBD()
        self.data = list() # list of processed depth images and actions taken (I_t, a_t)
        self.idx = 0
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
        return (c_img, c_img, c_img)


    def collect_data(self):
        """Does one instance of data collection, then saves.
        """
        (c_img, d_img, d_img_proc) = self.get_images()
        pth1 = os.path.join(TARGET_DIR, 'c_img_{}.png'.format(str(self.idx).zfill(3)))
        pth2 = os.path.join(TARGET_DIR, 'd_img_{}.png'.format(str(self.idx).zfill(3)))
        pth3 = os.path.join(TARGET_DIR, 'd_img_proc_{}.png'.format(str(self.idx).zfill(3)))
        self.data.append({"image": d_img_proc, "action": None})
        self.idx += 1
        cv2.imwrite(pth1, c_img)
        cv2.imwrite(pth2, d_img)
        cv2.imwrite(pth3, d_img_proc)

    def record_action(self, action): 
        """Saves a_t, the action vector at time t = self.idx: [grasp_x, grasp_y, angle, length]
        """
        self.data[self.idx - 1]["action"] = {'x': action[0], 'y': action[1], 'angle': action[2], 'length': action[3]}

    def pickle(self):
        with open(os.path.join(TARGET_DIR, 'rollout.pkl'), 'wb') as handle:
            pickle.dump(self.data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def display_grasp(self, image, cX, cY, angle, length, grasp_num, total_grasp_num):
        """Shows the user where to grasp and how to execute it in an image.
        """
        # Right now we assume we only have the 4 cardinal directions
        dX, dY = 0, 0
        if angle == 0: 
            dX = 50
        elif angle == 90: 
            dY = 50
        elif angle == 180:
            dX = -50
        else:
            dY = -50
        cv2.arrowedLine(image, (cX, cY), (cX + dX, cY + dY), (255, 0, 0), 3)
        cv2.putText(img=image, 
                    text="{} cm".format(length), 
                    org=(cX+30,cY+30), 
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1, 
                    color=(255,255,255), 
                    thickness=2)
        cv2.imshow("Execute grasp {}/{} as shown, then press any key".format(str(grasp_num), str(total_grasp_num)), image)
        cv2.waitKey() # wait for a key press to continue execution
        cv2.destroyAllWindows()

    def display_episode(self, image, episode_num):
        """Shows an image between data collection episodes notifying the user to reset the blanket.
        """
        black_bg = np.zeros(image.shape)
        cv2.imshow("EPISODE {} STARTING. Please reset blanket position, then press any key.".format(str(episode_num)), black_bg)
        cv2.waitKey()
        cv2.destroyAllWindows()

NUM_EPISODES = 10
NUM_ACTIONS_PER_EPISODE = 20
VALID_ANGLES = [0, 90, 180, 270] # in degrees on the unit circle, where 0 degrees is the horizontal ("East") when facing the side of the bed
VALID_LENGTHS = [20] # in cm

if __name__ == "__main__":
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
    dc = DataCollector()
    dc.orient_robot()
    dc.collect_data() # record initial state
    for _episode in range(NUM_EPISODES):
        # (re)set the blanket to a random, not overly complex starting position (e.g. one gentle fold)
        dc.display_episode(dc.get_images()[0], _episode + 1)
        for _action in range(NUM_ACTIONS_PER_EPISODE):
            # tell/show human what action to take. Future extension: incorporate active learning here
            # sample angle and length
            angle = VALID_ANGLES[np.random.randint(len(VALID_ANGLES))]
            length = VALID_LENGTHS[np.random.randint(len(VALID_LENGTHS))]
            # for now, it just tells us to grasp the corner, which should be marked with red.
            current_rgb = dc.get_images()[0]
            (img, x, y) = red_contour(current_rgb)
            # show the user where and how to pull
            dc.display_grasp(img, x, y, angle, length, _action + 1, NUM_ACTIONS_PER_EPISODE)
            action = [x, y, angle, length]
            dc.record_action(action)
            # take image I_t+1
            dc.collect_data()
    dc.pickle()
