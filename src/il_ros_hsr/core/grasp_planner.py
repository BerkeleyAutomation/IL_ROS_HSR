from hsrb_interface import geometry
import hsrb_interface
from geometry_msgs.msg import PoseStamped, Point, WrenchStamped
import geometry_msgs
import controller_manager_msgs.srv
from cv_bridge import CvBridge, CvBridgeError
import IPython, cv2, os, time, sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

import numpy as np
import numpy.linalg as LA
from numpy.random import normal
from tf import TransformListener
import tf, rospy
from image_geometry import PinholeCameraModel as PCM

# will remove later
from il_ros_hsr.core.sensors import  RGBD, Gripper_Torque, Joint_Positions
from il_ros_hsr.core.joystick import  JoyStick
from il_ros_hsr.core.rgbd_project import RGBD_Project


class GraspPlanner():

    def __init__(self):
        """
        """
        NUM_GRASPS = 40
        GRIPPER_WIDTH = 40 #MM
        self.cam_project = RGBD_Project()


    def find_mean_depth(self,d_img):
        """Used in `gripper.find_region_pick_net(...)`.
        """
        indx = np.nonzero(d_img)
        mean = np.mean(d_img[indx])
        return mean


    def find_max_depth(self,d_img):
        """
        """
        indx = np.nonzero(d_img)
        mean = np.max(d_img[indx])
        return mean


    def get_deprojected_points(self,points,d_img,c_img):
        """
        """
        p_0 = points[0]
        p_1 = points[1]
        points = []

        for x in range(int(p_0[0]),int(p_1[0])):
            for y in range(int(p_0[1]),int(p_1[1])):
                z = d_img[x,y]
                if z > 0.0:
                    pose = self.cam_project.deproject_pose((x,y,z))
                points.append(pose)
        return points


    def compute_grasp(self,points,d_img,c_img):
        """
        """
        points = self.get_deprojected_points(points,d_img,c_img)


if __name__ == "__main__":
    pass
