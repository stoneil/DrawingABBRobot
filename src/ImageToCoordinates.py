import cv2
import argparse
import numpy as np
from os import listdir
from os.path import isfile, join
from Robot_Controller import Robot_Controller

# conversion function (pixels -> mm)
def image2world(i, j):
    x = i * 3.175
    y = j * 3.175
    return [x, y]

def drawColor(img, color):
    count = 0
    current_count = 0
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if not np.array_equal(img[i][j], [255, 255, 255]):
                count = count + 1
    R.set_tool(R.tool_poses[color])
    R.set_cartesian_euler([0, 0, R.draw_height], R.draw_euler_orientation)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            # print(str(img[i][j]))
            if not np.array_equal(img[i][j], [255, 255, 255]):
                print('i: ' + str(i) + '\tj: ' + str(j) + '\tpixel val: ' + str(img[i][j]))
                xy_point = image2world(i, j)
                R.draw_point(xy_point)
                current_count = current_count + 1
                print "Remaining points in " + color + ": " + str(count - current_count)

# Image Setup for magenta image
"""
np.set_printoptions(threshold=np.inf)
parser = argparse.ArgumentParser(description='...')
parser.add_argument('--limit-image-size', default=0, type=int, help="Limit the image size (0 = no limits)")
parser.add_argument('img_path', nargs='?', default="../images/cbputnam_resized_magenta.jpg")
args = parser.parse_args()
magenta_img = cv2.imread(args.img_path)
"""

mypath='../images/final_putnam_images'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
    images[n] = cv2.imread(join(mypath,onlyfiles[n]))
print("here")
# Init Robot_Controller class
R = Robot_Controller()
print("there")



# Draw the stuffs!

drawColor(images[0], 'BLACK')
drawColor(images[1], 'YELLOW')
drawColor(images[2], 'MAGENTA')
drawColor(images[3], 'CYAN')
