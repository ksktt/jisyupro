#! /usr/bin/env python

from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def rotation():
    i = 600
    #if i = 600 left rotation
    #if i = 150 right rotation
    pwm.set_pwm(4, 0, 150)
    pwm.set_pwm(5, 0, 150)
    pwm.set_pwm(6, 0, 150)
    """
    try:
        while True:
            pwm.set_servo_pulse(4, 150)
            pwm.set_servo_pulse(5, 150)
            pwm.set_servo_pulse(6, 150)
            pass
    except KeyInterruption:
        pwm.set_servo_pulse(4, 0)
        pwm.set_servo_pulse(5, 0)
        pwm.set_servo_pulse(6, 0)
    """

if __name__ == "__main__":
    print("start right rotating ...")
    rotation()
