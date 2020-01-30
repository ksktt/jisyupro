#from temperature import tempMeasurement
import path_detection
from calculateGoalPos import calculate
#from temperature import temperature
from moveX import moveToX
from moveY import moveToY
import numpy as np
import sys

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

#args = sys.argv

x_pos, y_pos = calculate()
x_pos = x_pos / 100
y_pos = y_pos / 100
#print(x_pos, y_pos)

import dht11
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

    if result.temperature > 10:
        print("break")
        break

    time.sleep(1.0)

#goal_pos = [float(args[1]), float(args[2])]
goal_pos = [x_pos, y_pos]
print(goal_pos)

final_path = path_detection.main(goal_pos)
final_path = np.flipud(final_path)
print("decide final path")

for i in range(len(final_path)):
    if i == len(final_path) - 1:
        move_vec = goal_pos - final_path[i]
    else:
        move_vec = final_path[i+1] - final_path[i]

    print("follow x pos")
    moveToX(move_vec[0])
    print("follow y pos")
    moveToY(move_vec[1])

print("arrive at goal")
