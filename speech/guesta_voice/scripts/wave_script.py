#!/usr/bin/env python

# Copyright (c) 2013-2015, Rethink Robotics
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the Rethink Robotics nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import argparse
import math
import random
import time
import threading
from std_msgs.msg import String

import rospy

from std_msgs.msg import (
    UInt16,
)

import baxter_interface

from baxter_interface import CHECK_VERSION


class Wave(object):

    def __init__(self):
        """
        'Wobbles' both arms by commanding joint velocities sinusoidally.
        """
        self._pub_rate = rospy.Publisher('robot/joint_state_publish_rate',
                                         UInt16, queue_size=10)
        self._left_arm = baxter_interface.limb.Limb("left")
        self._right_arm = baxter_interface.limb.Limb("right")
        self._left_joint_names = self._left_arm.joint_names()
        self._right_joint_names = self._right_arm.joint_names()

        # control parameters
        self._rate = 1000.0  # Hz

        print("Getting robot state... ")
        self._rs = baxter_interface.RobotEnable(CHECK_VERSION)
        self._init_state = self._rs.state().enabled
        print("Enabling robot... ")
        self._rs.enable()

        # set joint state publishing to 500Hz
        self._pub_rate.publish(self._rate)
        self._left_arm.set_joint_position_speed(0.5)
        self._right_arm.set_joint_position_speed(0.5)
       
        #self._right_arm.set_joint_position_speed(0.75)

    def _reset_control_modes(self):
        rate = rospy.Rate(self._rate)
        for _ in xrange(100):
            if rospy.is_shutdown():
                return False
            self._left_arm.exit_control_mode()
            self._right_arm.exit_control_mode()
            self._pub_rate.publish(100)  # 100Hz default joint state rate
            rate.sleep()
        return True

    def set_neutral(self):
        """
        Sets both arms back into a neutral pose.
        """
        print("Moving to neutral pose...")
        self._left_arm.move_to_neutral()
        self._right_arm.move_to_neutral()

    def clean_shutdown(self):
        print("\nExiting example...")
        #return to normal
        self._reset_control_modes()
        self.set_neutral()
        if not self._init_state:
            print("Disabling robot...")
            self._rs.disable()
        return True

    def wave(self):
        #self.set_neutral()
        """
        Performs the wobbling of both arms.
        """
	limb = baxter_interface.Limb('right')
    
	# angles = limb.joint_angles()
	# angles['right_s0']=-0.75
	# angles['right_s1']=0.0
	# angles['right_e0']=0.0
	# angles['right_e1']=0.0
	# angles['right_w0']=0.0
	# angles['right_w1']=0.0
	# angles['right_w2']=0.0
	# print(angles)
	# limb.move_to_joint_positions(angles)
	wave_1 = {'right_s0': -0.459, 'right_s1': -0.202, 'right_e0': 1.807, 'right_e1': 1.714, 'right_w0': -0.906, 'right_w1': -1.545, 'right_w2': -0.276}
	wave_2 = {'right_s0': -0.395, 'right_s1': -0.202, 'right_e0': 1.831, 'right_e1': 1.981, 'right_w0': -1.979, 'right_w1': -1.100, 'right_w2': -0.448}
		
	for _move in range(3):
		limb.move_to_joint_positions(wave_1, timeout=2, threshold=0.008)
		limb.move_to_joint_positions(wave_2,timeout=2, threshold=0.008)

	# limb = baxter_interface.Limb('left')
        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=-1.3
        # angles['left_e0']=0.0
        # angles['left_e1']=0.0
        # angles['left_w0']=-1.8
        # angles['left_w1']=0.0
        # angles['left_w2']=-1.8
        # print(angles)
        # limb.move_to_joint_positions(angles)

        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=-1.31
        # angles['left_e0']=0.0
        # angles['left_e1']=0.0
        # angles['left_w0']=-1.8
        # angles['left_w1']=1.2
        # angles['left_w2']=-1.8
        # print(angles)
        # limb.move_to_joint_positions(angles)

        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=-1.3
        # angles['left_e0']=0.0
        # angles['left_e1']=0.0
        # angles['left_w0']=-1.8
        # angles['left_w1']=-0.9
        # angles['left_w2']=-1.8
        # print(angles)
        # limb.move_to_joint_positions(angles)
        self.set_neutral()

    def bigwave(self):
        #self.set_neutral()
        """
        Performs the wobbling of both arms.
        """
        limb = baxter_interface.Limb('left')
        limb.set_joint_position_speed(0.5)
        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=-1.3
        # angles['left_e0']=0.0
        # angles['left_e1']=0.0
        # angles['left_w0']=-1.8
        # angles['left_w1']=0.0
        # angles['left_w2']=-1.8
        # print(angles)
        #limb.move_to_joint_positions(angles)
        wave_1 = {'left_s0': 0.0, 'left_s1': -1.3, 'left_e0': 0.0, 'left_e1': 0.0, 'left_w0': -1.8, 'left_w1': 1.2, 'left_w2': -1.8}
        wave_2 = {'left_s0': 0.0, 'left_s1': -1.3, 'left_e0': 0.0, 'left_e1': 0.0, 'left_w0': -1.8, 'left_w1':0, 'left_w2': -1.8}
		
        for _move in range(3):
            limb.move_to_joint_positions(wave_1)
            limb.move_to_joint_positions(wave_2)
        
       # self.set_neutral()

    def nod(self):
        for _move in range(3):
            baxter_interface.Head().command_nod()


    def dance(self):
        for _move in range(3):
            baxter_interface.Head().command_nod()


    def sayno(self):
        for _move in range(3):
            baxter_interface.Head().set_pan(-1, speed=0.5, timeout=10)
            baxter_interface.Head().set_pan(1, speed=0.5, timeout=10)

    def comehere(self):
        
        """
        Performs the wobbling of both arms.
        """
        limb = baxter_interface.Limb('left')
        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=0.0
        # angles['left_e0']=-2.8
        # angles['left_e1']=0.0
        # angles['left_w0']=0.0
        # angles['left_w1']=0.0
        # angles['left_w2']=0.0
        # print(angles)
        #limb.move_to_joint_positions(angles)
        wave_1 = {'left_s0': 0.0, 'left_s1': 0.0, 'left_e0': -2.8, 'left_e1': 0.0, 'left_w0': 0.0, 'left_w1': 1.0, 'left_w2': 0.0}
        wave_2 = {'left_s0': 0.0, 'left_s1': 0.0, 'left_e0': -2.8, 'left_e1': 0.0, 'left_w0': 0.0, 'left_w1': 00, 'left_w2': 0.0}
		
        for _move in range(3):
            limb.move_to_joint_positions(wave_1)
            limb.move_to_joint_positions(wave_2)
        
        self.set_neutral()
        # limb = baxter_interface.Limb('left')
        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=0.0
        # angles['left_e0']=-2.8
        # angles['left_e1']=0.0
        # angles['left_w0']=0.0
        # angles['left_w1']=0.0
        # angles['left_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)

        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=0.0
        # angles['left_e0']=-2.8
        # angles['left_e1']=0.0
        # angles['left_w0']=0.0
        # angles['left_w1']=1.0
        # angles['left_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)

        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=0.0
        # angles['left_e0']=-2.8
        # angles['left_e1']=0.0
        # angles['left_w0']=0.0
        # angles['left_w1']=0.0
        # angles['left_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)

    def firstbump(self):
        self.set_neutral()
        """
        Performs the wobbling of both arms.
        """
        # limb = baxter_interface.Limb('left')
        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=0.0
        # angles['left_e0']=-2.8
        # angles['left_e1']=0.0
        # angles['left_w0']=0.0
        # angles['left_w1']=0.0
        # angles['left_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)
        # wave_1 = {'left_s0': 0.0, 'left_s1': 0.0, 'left_e0': -2.8, 'left_e1': 0.0, 'left_w0': 0.0, 'left_w1': 1.0, 'left_w2': 0.0}
        # wave_2 = {'left_s0': 0.0, 'left_s1': 0.0, 'left_e0': -2.8, 'left_e1': 0.0, 'left_w0': 0.0, 'left_w1': 00, 'left_w2': 0.0}
		
        # for _move in range(3):
            # limb.move_to_joint_positions(wave_1)
            # limb.move_to_joint_positions(wave_2)

        limb = baxter_interface.Limb('right')
        angles = limb.joint_angles()
        angles['right_s0']=1.0
        angles['right_s1']=-0.2
        angles['right_e0']=0.0
        angles['right_e1']=0.0
        angles['right_w0']=0.0
        angles['right_w1']=0.0
        angles['right_w2']=0.0
        print(angles)
        limb.move_to_joint_positions(angles)

        angles = limb.joint_angles()
        angles['right_s0']=1.0
        angles['right_s1']=-0.2
        angles['right_e0']=0.0
        angles['right_e1']=0.0
        angles['right_w0']=0.0
        angles['right_w1']=0.0
        angles['right_w2']=0.0
        print(angles)
        limb.move_to_joint_positions(angles)

        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=0.0
        # angles['left_e0']=-2.8
        # angles['left_e1']=0.0
        # angles['left_w0']=0.0
        # angles['left_w1']=0.0
        # angles['left_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)

    def shakehands(self):

        """
        Performs the wobbling of both arms.
        """
        # limb = baxter_interface.Limb('left')
        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=0.0
        # angles['left_e0']=-2.8
        # angles['left_e1']=0.0
        # angles['left_w0']=0.0
        # angles['left_w1']=0.0
        # angles['left_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)
        # wave_1 = {'left_s0': 0.0, 'left_s1': 0.0, 'left_e0': -2.8, 'left_e1': 0.0, 'left_w0': 0.0, 'left_w1': 1.0, 'left_w2': 0.0}
        # wave_2 = {'left_s0': 0.0, 'left_s1': 0.0, 'left_e0': -2.8, 'left_e1': 0.0, 'left_w0': 0.0, 'left_w1': 00, 'left_w2': 0.0}
		
        # for _move in range(3):
            # limb.move_to_joint_positions(wave_1)
            # limb.move_to_joint_positions(wave_2)

        limb = baxter_interface.Limb('right')
        angles = limb.joint_angles()
        angles['right_s0']=1.0
        angles['right_s1']=0.0
        angles['right_e0']=1.6
        angles['right_e1']=0.0
        angles['right_w0']=0.0
        angles['right_w1']=0.0
        angles['right_w2']=0.0
        print(angles)
        limb.move_to_joint_positions(angles)
        time.sleep(1)

        self.set_neutral()
        # angles = limb.joint_angles()
        # angles['right_s0']=1.0
        # angles['right_s1']=0.0
        # angles['right_e0']=0.0
        # angles['right_e1']=0.0
        # angles['right_w0']=0.0
        # angles['right_w1']=0.0
        # angles['right_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)

        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=0.0
        # angles['left_e0']=-2.8
        # angles['left_e1']=0.0
        # angles['left_w0']=0.0
        # angles['left_w1']=0.0
        # angles['left_w2']=0.0
        # print(angles)left
        # limb.move_to_joint_positions(angles)
    
    def performDAB(self):

        """
        Performs the wobbling of both arms.
        """
        limb = baxter_interface.Limb('left')
        angles = limb.joint_angles()
        angles['left_s0']=1.0
        angles['left_s1']=-0.4
        angles['left_e0']=-3.5
        angles['left_e1']=0.0
        angles['left_w0']=0.0
        angles['left_w1']=0.0
        angles['left_w2']=0.0
        print(angles)
        limb.move_to_joint_positions(angles)
        # wave_1 = {'left_s0': 0.0, 'left_s1': 0.0, 'left_e0': -2.8, 'left_e1': 0.0, 'left_w0': 0.0, 'left_w1': 1.0, 'left_w2': 0.0}
        # wave_2 = {'left_s0': 0.0, 'left_s1': 0.0, 'left_e0': -2.8, 'left_e1': 0.0, 'left_w0': 0.0, 'left_w1': 00, 'left_w2': 0.0}
		
        # for _move in range(3):
            # limb.move_to_joint_positions(wave_1)
            # limb.move_to_joint_positions(wave_2)

        limb = baxter_interface.Limb('right')
        angles = limb.joint_angles()
        angles['right_s0']=1.0
        angles['right_s1']=-0.4
        angles['right_e0']=2.5
        angles['right_e1']=2.5
        angles['right_w0']=0.0
        angles['right_w1']=1.2
        angles['right_w2']=0.0
        print(angles)
        limb.move_to_joint_positions(angles)
        time.sleep(1)

        self.set_neutral()
        # angles = limb.joint_angles()
        # angles['right_s0']=1.0
        # angles['right_s1']=0.0
        # angles['right_e0']=0.0
        # angles['right_e1']=0.0
        # angles['right_w0']=0.0
        # angles['right_w1']=0.0
        # angles['right_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)

        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=0.0
        # angles['left_e0']=-2.8
        # angles['left_e1']=0.0
        # angles['left_w0']=0.0
        # angles['left_w1']=0.0
        # angles['left_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)

    def rightarmwhy(self):
        #self.set_neutral()
        """
        Performs the wobbling of both arms.
        """
        # limb = baxter_interface.Limb('left')
        # angles = limb.joint_angles()
        # angles['left_s0']=0.0
        # angles['left_s1']=0.0
        # angles['left_e0']=-2.8
        # angles['left_e1']=0.0
        # angles['left_w0']=0.0
        # angles['left_w1']=0.0
        # angles['left_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)
        # wave_1 = {'left_s0': 0.0, 'left_s1': 0.0, 'left_e0': -2.8, 'left_e1': 0.0, 'left_w0': 0.0, 'left_w1': 1.0, 'left_w2': 0.0}
        # wave_2 = {'left_s0': 0.0, 'left_s1': 0.0, 'left_e0': -2.8, 'left_e1': 0.0, 'left_w0': 0.0, 'left_w1': 00, 'left_w2': 0.0}
		
        # for _move in range(3):
            # limb.move_to_joint_positions(wave_1)
            # limb.move_to_joint_positions(wave_2)

        limb = baxter_interface.Limb('right')
        angles = limb.joint_angles()
        angles['right_s0']=-1.0
        angles['right_s1']=-0.4
        angles['right_e0']=3.5
        angles['right_e1']=0
        angles['right_w0']=0
        angles['right_w1']=0
        angles['right_w2']=0.0
        print(angles)
        limb.move_to_joint_positions(angles)
    #    time.sleep(1)


        angles = limb.joint_angles()
        angles['right_s0']=-1.0
        angles['right_s1']=1.0
        angles['right_e0']=3.5
        angles['right_e1']=2.0
        angles['right_w0']=0
        angles['right_w1']=-1
        angles['right_w2']=0.0
        print(angles)
        limb.move_to_joint_positions(angles)

        # limb = baxter_interface.Limb('left')
        # angles = limb.joint_angles()
        # angles['left_s0']=1.0
        # angles['left_s1']=0.4
        # angles['left_e0']=-3.5
        # angles['left_e1']=0.0
        # angles['left_w0']=0.0
        # angles['left_w1']=0.0
        # angles['left_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)

        # angles = limb.joint_angles()
        # angles['left_s0']=1.0
        # angles['left_s1']=0.4
        # angles['left_e0']=-3.5
        # angles['left_e1']=2.0
        # angles['left_w0']=0.0
        # angles['left_w1']=0.0
        # angles['left_w2']=0.0
        # print(angles)
        # limb.move_to_joint_positions(angles)

    def leftarmwhy(self):
        self.set_neutral()
        """
        Performs the wobbling of both arms.
        """
        limb = baxter_interface.Limb('left')
        angles = limb.joint_angles()
        angles['left_s0']=1.0
        angles['left_s1']=-0.4
        angles['left_e0']=-3.5
        angles['left_e1']=0.0
        angles['left_w0']=0.0
        angles['left_w1']=0.0
        angles['left_w2']=0.0
        print(angles)
        limb.move_to_joint_positions(angles)

        angles = limb.joint_angles()
        angles['left_s0']=1.0
        angles['left_s1']=1.0
        angles['left_e0']=-3.5
        angles['left_e1']=2
        angles['left_w0']=0
        angles['left_w1']=-1
        angles['left_w2']=0
        print(angles)
        limb.move_to_joint_positions(angles)

    def rightdab(self):
        #self.set_neutral()
        """
        Performs the wobbling of both arms.
        """
        limb = baxter_interface.Limb('left')
        angles = limb.joint_angles()
        angles['left_s0']=1.0
        angles['left_s1']=-0.4
        angles['left_e0']=-3.5
        angles['left_e1']=0.0
        angles['left_w0']=0.0
        angles['left_w1']=0.0
        angles['left_w2']=0.0
        print(angles)
        limb.move_to_joint_positions(angles)

    def leftdab(self):
        limb = baxter_interface.Limb('right')
        angles = limb.joint_angles()
        # angles['right_s0']=1.0
        # angles['right_s1']=-0.4
        # angles['right_e0']=2.5
        # angles['right_e1']=2.5
        # angles['right_w0']=0.0
        # angles['right_w1']=0.0
        # angles['right_w2']=0.0
        time.sleep(2)
        angles = limb.joint_angles()
        angles['right_s0']=1.0
        angles['right_s1']=0.0
        angles['right_e0']=2.5
        angles['right_e1']=1.0
        angles['right_w0']=0.0
        angles['right_w1']=0.0
        angles['right_w2']=0.0
        print(angles)
        limb.move_to_joint_positions(angles)
        time.sleep(10)
        angles = limb.joint_angles()
        angles['right_s0']=0.0
        angles['right_s1']=0.0
        angles['right_e0']=2.5
        angles['right_e1']=2.5
        angles['right_w0']=0.0
        angles['right_w1']=0.0
        angles['right_w2']=0.0
        print(angles)
        limb.move_to_joint_positions(angles)

        

        time.sleep(1)

        #self.set_neutral()

    def highfive(self):
        self.set_neutral()
        """
        Performs a high five
        """
        limb = baxter_interface.Limb('left')
        angles = limb.joint_angles()
        angles['left_s0']=0
        angles['left_s1']=-0.9
        angles['left_e0']=0
        angles['left_e1']=1.0
        angles['left_w0']=0.0
        angles['left_w1']=-1.3
        angles['left_w2']=0.0
        print(angles)
        
        
        vel_0 = {'left_s0': 1, 'left_s1': 1, 'left_e0': 1, 'left_e1': 1, 'left_w0': 1, 'left_w1': 1, 'left_w2': 1}
        #limb.set_joint_velocities(vel_0);
        cur_vel = limb.joint_velocities()
        limb.set_joint_torques(vel_0)
        print(cur_vel)


        limb.move_to_joint_positions(angles, timeout=20)
        time.sleep(2)


class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self._pub_rate = rospy.Publisher('robot/joint_state_publish_rate',
                                         UInt16, queue_size=10)
      self._left_arm = baxter_interface.limb.Limb("left")
      self._right_arm = baxter_interface.limb.Limb("right")
      self._left_joint_names = self._left_arm.joint_names()
      self._right_joint_names = self._right_arm.joint_names()
      # control parameters
      self._rate = 500.0  # Hz
      print("Getting robot state... ")
      self._rs = baxter_interface.RobotEnable(CHECK_VERSION)
      self._init_state = self._rs.state().enabled
      print("Enabling robot... ")
      self._rs.enable()

        # set joint state publishing to 500Hz
        #self._pub_rate.publish(self._rate)
   def run(self):
      global threadLock
      print "Starting " + self.name
      if self.name =='leftwave':
            baxter_wave = Wave()
            baxter_wave.leftarmwhy()

      if self.name =='rightwave':
            print "rightwave"
            baxter_wave = Wave()
            baxter_wave.rightarmwhy()

      if self.name =='rightdab':
            print "rightdab"
            baxter_wave = Wave()
            baxter_wave.rightdab()
      if self.name =='leftdab':
            print "leftdab"
            baxter_wave = Wave()
            baxter_wave.leftdab()



   def set_neutral(self):
        """
        Sets both arms back into a neutral pose.
        """
        print("Moving to neutral pose...")
        self._left_arm.move_to_neutral()
        self._right_arm.move_to_neutral()    

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print "%s: %s" % (threadName, time.ctime(time.time()))
      counter -= 1

threadLock =0;

def debug(str):
    print (str)

def speech_callback(data):
    #debug(str(data.data))
    print data.data
    if data.data=="wave":
         baxter_wave = Wave()
         baxter_wave.wave()
    if data.data=="big wave":
         baxter_wave = Wave()
         baxter_wave.bigwave()
    if data.data=="":
         baxter_wave = Wave()
         baxter_wave.bigwave()
    if data.data=="hand shake":
         baxter_wave = Wave()
         baxter_wave.shakehands()
    if data.data=="come here":
         baxter_wave = Wave()
         baxter_wave.comehere()
    if data.data=="fist bump":
         baxter_wave = Wave()
         baxter_wave.firstbump()
    if data.data=="high five":
         baxter_wave = Wave()
         baxter_wave.highfive()
    if data.data=="dab":
        threadLock = threading.Lock()
        threads = []

        # Create new threads
        thread1 = myThread(1, "leftdab", 1)
        thread2 = myThread(2, "rightdab", 2)

        # Start new Threads
        thread1.start()
        thread2.start()

        # Add threads to thread list
        threads.append(thread1)
        threads.append(thread2)

        # Wait for all threads to complete
        for t in threads:
            t.join()
        print "Exiting Main Thread"
        print("understand.")
        
    if data.data=="understand":
        threadLock = threading.Lock()
        threads = []

        # Create new threads
        thread1 = myThread(1, "leftwave", 1)
        thread2 = myThread(2, "rightwave", 2)

        # Start new Threads
        thread1.start()
        thread2.start()

        # Add threads to thread list
        threads.append(thread1)
        threads.append(thread2)

        # Wait for all threads to complete
        for t in threads:
            t.join()
        print "Exiting Main Thread"
        print("understand.")

def main():
    """RSDK Baxter Wave

    Commands Baxters arms to wave at the client
    """
    global threadLock
    arg_fmt = argparse.RawDescriptionHelpFormatter  
    parser = argparse.ArgumentParser(formatter_class=arg_fmt,
                                     description=main.__doc__)
    parser.parse_args(rospy.myargv()[1:])

    print("Initializing node... ")
    rospy.init_node("baxter_wave")

    baxter_wave = Wave()
    # rospy.on_shutdown(baxter_wave.clean_shutdown)
   
    
    # threadLock = threading.Lock()
    # threads = []

        # # Create new threads
    # thread1 = myThread(1, "leftdab", 1)
    # thread2 = myThread(2, "rightdab", 2)

        # # Start new Threads
    # thread1.start()
    # thread2.start()

        # # Add threads to thread list
    # threads.append(thread1)
    # threads.append(thread2)

        # # Wait for all threads to complete
    # for t in threads:
        # t.join()
    # print "Exiting Main Thread"
    # print("understand.")
    #rospy.Subscriber("/input/speech/commands",String,speech_callback)
    #rospy.spin()
# A Complete List of Gestures 
    #baxter_wave.leftdab()
    #baxter_wave.bigwave()
    #baxter_wave.comehere()
    # baxter_wave.firstbump()
    #baxter_wave.shakehands()
    baxter_wave.nod()
    baxter_wave.sayno()
    #baxter_wave.leftarmwhy()
    
    # threadLock = threading.Lock()
    # threads = []

    # # Create new threads
    # thread1 = myThread(1, "leftwave", 1)
    # thread2 = myThread(2, "rightwave", 2)

    # # Start new Threads
    # thread1.start()
    # thread2.start()

    # # Add threads to thread list
    # threads.append(thread1)
    # threads.append(thread2)

    # # Wait for all threads to complete
    # for t in threads:
        # t.join()
    # print "Exiting Main Thread"
    # print("Done.")

if __name__ == '__main__':
    main()