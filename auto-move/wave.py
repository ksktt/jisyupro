#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

def reading(sensor, TRIG_NUM, ECHO_NUM):
    TRIG = TRIG_NUM
    ECHO = ECHO_NUM

    if sensor == 0:
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.3)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
          signaloff = time.time()

        while GPIO.input(ECHO) == 1:
          signalon = time.time()

        timepassed = signalon - signaloff
        distance = timepassed * 17000
        return distance
        GPIO.cleanup()
    else:
        print "Incorrect usonic() function varible."

if __name__ == "__main__":
    while True:
        #print("front distance is ... {}".format(reading(0, 11, 13))) #on Board
        print("front distance is ... {}".format(reading(0, 17, 27)))
        #print("right distance is ... {}".format(reading(0, 16, 18))) #on Board
        #print("left distance is ... {}".format(reading(0, 29, 31))) #on Board
