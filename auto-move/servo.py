# /usr/bin/env python

from __future__ import division
import time
import Adafruit_PCA9685

from wave import reading

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def move(degree_1,degree_2):
    degree_1 = int(degree_1 * 5.27)
    degree_2 = int(degree_2 * 5.27)
    pwm.set_pwm(0, 0, degree_1)
    pwm.set_pwm(1, 0, degree_2)

def controller():
    #initialize angle
    degree1_pulse = 375 #0 degree
    degree2_pulse = 375 #0 degree
    pwm.set_pwm(0, 0, degree1_pulse)
    pwm.set_pwm(1, 0, degree2_pulse)

    #keyboard operations
    while True:
        val = raw_input('Enter operation type: ')
        if val == 'L':
            degree1_pulse = int(degree1_pulse + 15 * 225 / 90)
            pwm.set_pwm(0, 0, degree1_pulse)
            pwm.set_pwm(1, 0, degree2_pulse)
            print("distance is {}".format(reading(0, 17, 27)))

        elif val == 'l':
            degree1_pulse = int(degree1_pulse + 5 * 225 / 90)
            pwm.set_pwm(0, 0, degree1_pulse)
            pwm.set_pwm(1, 0, degree2_pulse)
            print("distance is {}".format(reading(0, 17, 27)))

        elif val == 'R':
            degree1_pulse = int(degree1_pulse - 15 * 225 / 90)
            pwm.set_pwm(0, 0, degree1_pulse)
            pwm.set_pwm(1, 0, degree2_pulse)
            print("distance is {}".format(reading(0, 17, 27)))

        elif val == 'r':
            degree1_pulse = int(degree1_pulse - 5 * 225 / 90)
            pwm.set_pwm(0, 0, degree1_pulse)
            pwm.set_pwm(1, 0, degree2_pulse)
            print("distance is {}".format(reading(0, 17, 27)))

        elif val == 'D':
            degree2_pulse = int(degree2_pulse + 15 * 225 / 90)
            pwm.set_pwm(0, 0, degree1_pulse)
            pwm.set_pwm(1, 0, degree2_pulse)
            print("distance is {}".format(reading(0, 17, 27)))

        elif val == 'd':
            degree2_pulse = int(degree2_pulse + 5 * 225 / 90)
            pwm.set_pwm(0, 0, degree1_pulse)
            pwm.set_pwm(1, 0, degree2_pulse)
            print("distance is {}".format(reading(0, 17, 27)))

        elif val == 'U':
            degree2_pulse = int(degree2_pulse - 15 * 225 / 90)
            pwm.set_pwm(0, 0, degree1_pulse)
            pwm.set_pwm(1, 0, degree2_pulse)
            print("distance is {}".format(reading(0, 17, 27)))

        elif val == 'u':
            degree2_pulse = degree2_pulse - 5 * 225 / 90
            pwm.set_pwm(0, 0, degree1_pulse)
            pwm.set_pwm(1, 0, degree2_pulse)
            print("distance is {}".format(reading(0, 17, 27)))

        elif val == "w":
            break

    #print(degree1_pulse, degree2_pulse)
    if degree1_pulse >= 375:
        degree1 = (degree1_pulse - 375) * 90 / 225 + 90
    elif degree1_pulse < 375:
        degree1 = 90 - (375 - degree1_pulse) * 90 / 225
    if degree2_pulse >= 375:
        degree2 = (degree2_pulse - 375) * 90 / 225 + 90
    elif degree2_pulse < 375:
        degree2 = 90 - (375 - degree2_pulse) * 90 / 225

    return degree1, degree2, reading(0, 17, 27)

if __name__ == '__main__':
    #print('start moving ...')
    #move(45, 45)
    #time.sleep(2)
    #move(135, 135)
    #time.sleep(2)
    #move(90, 60)
    #time.sleep(2)
    #print('finish ...')
    x_deg,y_deg,dis = controller()
    print("x {}, y {}, dis {}".format(x_deg, y_deg, dis))
