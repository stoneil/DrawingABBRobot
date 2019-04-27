'''
Class to inherits the Robot class in abb.py. This initializes starting position, tool data, and manages the paths for drawing images

Authors: Sean O'Neil
'''

import abb
from transforms3d.euler import euler2mat
from transforms3d.quaternions import mat2quat
from math import radians, cos, sin

class Robot_Controller(abb.Robot):

    def __init__(self, radius=167, colors=('RED','BLACK','AQUA','YELLOW','MAROON','ORANGE','DARK BLUE','GREEEN'),ip='127.0.0.1'):
        #abb.Robot.__init__(self,ip)
        self.colors = colors
        self.tool_poses = self.generate_tool_poses(radius)


    def generate_tool_poses(self, radius=167):
        poses_dict = dict()
        for i in range(0,8): # starts at the red marker and finds the poses for all the markers in an CCW direction
            rot_mat = euler2mat(0, radians(90), radians(22.5 + 45*i))
            marker_quat = mat2quat(rot_mat).tolist()
            x = radius*cos(radians(22.5 + 45*i))
            y = radius * sin(radians(22.5 + 45 * i))
            poses_dict[self.colors[i]] = [[x, y, 21.40], marker_quat]
        return poses_dict

