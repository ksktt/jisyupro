#!/usr/bin/env python
# -*- coding: utf-8 -*-

#https://qiita.com/mininobu/items/1ba0223af84be153b850

import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

def temperature():
    # read data using pin 14
    instance = dht11.DHT11(pin=14)

    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)

        time.sleep(1)

        if result.temperature > 5:
            break

print("finish")
