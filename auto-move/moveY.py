#! /usr/bin/env python

from __future__ import division
import time
import math
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def moveToY(y_pos):
    if y_pos >= 0:
        pwm.set_pwm(4, 0, int(150*math.sqrt(3)/2))
        pwm.set_pwm(5, 0, int(600*math.sqrt(3)/2))
        pwm.set_pwm(6, 0, 0)
        print("positive y pos")
        time.sleep(11*y_pos)
        pwm.set_pwm(4, 0, 0)
        pwm.set_pwm(5, 0, 0)
        pwm.set_pwm(6, 0, 0)
    else:
        pwm.set_pwm(5, 0, int(150*math.sqrt(3)/2))
        pwm.set_pwm(4, 0, int(600*math.sqrt(3)/2))
        pwm.set_pwm(6, 0, 0)
        print("negatice y pos")
        time.sleep(-10*y_pos)
        pwm.set_pwm(4, 0, 0)
        pwm.set_pwm(5, 0, 0)
        pwm.set_pwm(6, 0, 0)

if __name__=="__main__":
    y_pos = 0.1
    print("go straight 10cm")
    moveToY(y_pos)
