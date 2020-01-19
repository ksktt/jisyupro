# /usr/bin/env python

from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def move(degree_1,degree_2):
    degree_1 = int(degree_1 * 5.27)
    degree_2 = int(degree_2 * 5.27)
    pwm.set_pwm(0, 0, degree_1)
    pwm.set_pwm(1, 0, degree_2)

if __name__ == '__main__':
    print('start moving ...')
    move(45, 45)
    time.sleep(2)
    move(135, 135)
    time.sleep(2)
    move(90, 60)
    time.sleep(2)
    print('finish ...')
