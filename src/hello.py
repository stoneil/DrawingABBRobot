import abb

R = abb.Robot(ip='127.0.0.1')
R.set_joints([-90,0,0,0,0,0])
R.close()
