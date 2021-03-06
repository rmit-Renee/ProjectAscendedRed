#ros python api
import rospy
#baxter python api

import baxter_interface


rospy.init_node('Hello_Baxter')
limb = baxter_interface.Limb('right')

#get current angles
angles = limb.joint_angles()

#print them to test
print angles

angles['right_s0']=0.0
angles['right_s1']=0.0
angles['right_e0']=0.0
angles['right_e1']=0.0
angles['right_w0']=0.0
angles['right_w1']=0.0
angles['right_w2']=0.0

print angles

limb.move_to_joint_positions(angles)

wave_1 = {'right_s0': -0.459, 'right_s1': -0.202, 'right_e0': 1.807, 'right_e1': 1.714, 'right_w0': -0.906, 'right_w1': -1.545, 'right_w2': -0.276}

wave_2 = {'right_s0': -0.395, 'right_s1': -0.202, 'right_e0': 1.807, 'right_e1': 1.714, 'right_w0': -0.906, 'right_w1': -1.545, 'right_w2': -0.276}

for _move in range(3):
    limb.move_to_joint_positions(wave_1)
    limb.move_to_joint_positions(wave_2)

quit()
