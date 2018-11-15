import pickle, cv2, os
"""
Visualize collected data in the form of color images + actions taken.
"""
USERNAME = 'ryanhoque' # change as needed
TARGET_DIR = '/nfs/diskstation/{}/ssldata'.format(USERNAME)
pkl = pickle.load(open(os.path.join(DATAPATH, "rollout.pkl"), 'rb'))

def display_grasp(image, cX, cY, angle, length, grasp_num, total_grasp_num):
    """Shows the user where to grasp and how to execute it in an image.
    """
    # Right now we assume we only have the 4 cardinal directions
    dX, dY = 0, 0
    if angle == 0: 
        dX = 50
    elif angle == 90: 
        dY = -50
    elif angle == 180:
        dX = -50
    else:
        dY = 50
    cv2.arrowedLine(image, (cX, cY), (cX + dX, cY + dY), (255, 0, 0), 3)
    cv2.circle(image, (cX,cY), 20, (255, 0, 0), 2)
    cv2.line(image, (cX, cY - 30), (cX, cY + 30), (255, 0, 0), 2) # add crosshairs
    cv2.line(image, (cX - 30, cY), (cX + 30, cY), (255, 0, 0), 2)
    cv2.putText(img=image, 
                text="{} cm".format(length), 
                org=(cX+30,cY+30), 
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1, 
                color=(0,0,255), 
                thickness=2)
    cv2.imshow("Grasp {}/{}".format(str(grasp_num), str(total_grasp_num)), image)
    cv2.waitKey() # wait for a key press to continue execution
    cv2.destroyAllWindows()

NUM_EPISODES = 10
NUM_ACTIONS_PER_EPISODE = 20

for e in range(NUM_EPISODES):
    for a in range(NUM_ACTIONS_PER_EPISODE + 1):
		c_img = cv2.imread(os.path.join(DATAPATH, "d_img_proc_{}_{}.png".format(str(e + 1).zfill(2), str(a).zfill(3))))
		action = pkl[(e + 1, a)]['action']
		if action:
			display_grasp(c_img, action['x'], action['y'], action['angle'], action['length'], a + 1, NUM_ACTIONS_PER_EPISODE)
		else:
			cv2.imshow("", c_img)
			cv2.waitKey()
			cv2.destroyAllWindows()