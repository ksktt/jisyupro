#! /usr/bin/env python

from __future__ import division
import time
import math
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def moveToX(x_pos):
    if x_pos >= 0:
        pwm.set_pwm(4, 0, int((375+600)/2))
        pwm.set_pwm(5, 0, int((375+450)/2))
        pwm.set_pwm(6, 0, 150)
        print("positive x pos")
        time.sleep(12*x_pos)
        pwm.set_pwm(4, 0, 0)
        pwm.set_pwm(5, 0, 0)
        pwm.set_pwm(6, 0, 0)
    else:
        pwm.set_pwm(4, 0, int((300+375)/2))
        pwm.set_pwm(5, 0, int((150+375)/2))
        pwm.set_pwm(6, 0, 600)
        print("negative x pos")
        time.sleep(-8*x_pos)
        pwm.set_pwm(4, 0, 0)
        pwm.set_pwm(5, 0, 0)
        pwm.set_pwm(6, 0, 0)

if __name__=="__main__":
    x_pos = 0.1
    print("go right 10cm")
    moveToX(x_pos)
