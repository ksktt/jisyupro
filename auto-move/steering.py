#! /usr/bin/env python

from __future__ import division
import time
import math
import Adafruit_PCA9685
import straight
import left
import lef45
import right
import right45

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def direction(mode):
    if -1 <= mode and mode < -0.75:
        left.moveToLeft()
    elif -0.75 <= mode and mode < -0.25:
        left45.moveToLeft45()
    elif -0.25 <= mode and mode < 0.25:
        straight.moveToStraight()
    elif 0.25 <= mode and mode < 0.75:
        right45.moveToRight45()
    else:
        right.moveToRoight()
