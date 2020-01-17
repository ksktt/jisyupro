#! /usr/bin/env python
from __future__ import division
import time
import math
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def moveToLeft():
    try:
        while True:
            pwm.set_pwm(4, 0, int((150+375)/2))
            pwm.set_pwm(5, 0, int((150+375)/2))
            pwm.set_pwm(6, 0, 600)
            pass
    except KeyboardInterrupt:
        pwm.set_pwm(4, 0, 0)
        pwm.set_pwm(5, 0, 0)
        pwm.set_pwm(6, 0, 0)

if __name__ == "__main__":
    print("go left")
    moveToLeft()    
