#! /usr/bin/env python

from __future__ import division
import time
import math
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def moveToRight45():
    #servo_min = 150, servo_max = 600
    pwm.set_pwm(5, 0, int((375+600)*(-1+math.sqrt(3))/4))
    pwm.set_pwm(4, 0, int((375+600)*(1+math.sqrt(3))/4))
    pwm.set_pwm(6, 0, int((150+375)/2))

def test():
    pwm.set_pwm(4, 0, int((375+600)*(1+math.sqrt(3))/4))
    pwm.set_pwm(5, 0, int((200)*(-1+math.sqrt(3))/4))
    pwm.set_pwm(6, 0, 150)

if __name__ == "__main__":
    try:
        while True:
            test()
            pass
    except KeyboardInterrupt:
        pwm.set_pwm(4, 0, 0)
        pwm.set_pwm(5, 0, 0)
        pwm.set_pwm(6, 0, 0)
