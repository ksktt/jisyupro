#! /usr/bin/env python

from __future__ import division
import time
import math
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def moveToStraight():
    i = 150 #servo_min = 150, servo_max = 600
    try:
        while True:
            pwm.set_pwm(4, 0, int(i*math.sqrt(3)/2))
            pwm.set_pwm(5, 0, int((750 - i)*math.sqrt(3)/2))
            pwm.set_pwm(6, 0, 0)
            pass
    except KeyboardInterrupt:
        pwm.set_pwm(4, 0, 0)
        pwm.set_pwm(5, 0, 0)
        pwm.set_pwm(6, 0, 0)
if __name__ == "__main__":
    print("go straight ...")
    moveToStraight()
