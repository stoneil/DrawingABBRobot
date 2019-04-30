'''
Class to inherits the Robot class in abb.py. This initializes starting position, tool data, and manages the paths for drawing images

Author: Sean O'Neil
'''

import abb
from transforms3d.euler import euler2mat
from transforms3d.quaternions import mat2quat
from math import radians, cos, sin

class Robot_Controller(abb.Robot):

    def __init__(self, radius=167, colors=('RED','BLACK','CYAN','YELLOW','MAGENTA','ORANGE','DARK BLUE','GREEN'),ip='127.0.0.1'):
        abb.Robot.__init__(self,ip)

        self.colors = colors
        self.tool_poses = self.generate_tool_poses(radius)
        self.canvas_wobj_pose = [[-215.9, -1022.2, 1], [0, 1, 0, 0]]

        self.set_tool(self.tool_poses['RED'])
        self.set_workobject(self.canvas_wobj_pose)
        self.set_zone(zone_key='z0', point_motion=True)
        self.set_speed([100,50,50,50])
        # initial position above drawing
        self.draw_euler_orientation = [0, 0, -90]
        self.draw_height = -20
        self.set_joints([-90,0,0,0,0,0])
        self.set_joints([-102.99, 52.62, 12.32, 165.71, 65.62, 163.5])
        self.set_cartesian_euler([0, 0, self.draw_height], self.draw_euler_orientation)



    # Generates the 8 tool poses automatically so that they can be switched between
    def generate_tool_poses(self, radius=169.9):
        poses_dict = dict()
        for i in range(0,8): # starts at the red marker and finds the poses for all the markers in an CCW direction
            rot_mat = euler2mat(0, radians(90), radians(22.5 + 45*i))
            marker_quat = mat2quat(rot_mat).tolist()
            x = radius*cos(radians(22.5 + 45*i))
            y = radius * sin(radians(22.5 + 45 * i))
            poses_dict[self.colors[i]] = [[x, y, 21.40], marker_quat]
        return poses_dict

    def set_cartesian_euler(self, position, euler_angles):
        rot_mat = euler2mat(radians(euler_angles[0]), radians(euler_angles[1]), radians(euler_angles[2]))
        orientation = mat2quat(rot_mat).tolist()
        pose = [position, orientation]
        self.set_cartesian(pose)

    def draw_point(self, xy_point):
        self.set_cartesian_euler([xy_point[0], xy_point[1], self.draw_height], self.draw_euler_orientation)
        self.set_cartesian_euler([xy_point[0], xy_point[1], 0], self.draw_euler_orientation)
        self.set_cartesian_euler([xy_point[0], xy_point[1], self.draw_height], self.draw_euler_orientation)

    def switch2tool(self, color):
        self.set_tool(self.tool_poses[color])
        self.set_cartesian_euler([0, 0, self.draw_height], self.draw_euler_orientation)