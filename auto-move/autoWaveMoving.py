#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wave import reading
import straight
import rotation
import stop
import left
import right
import left45
import right45
import time
import back

def control():
    try:
        while True:
            frontDistance = reading(0, 11, 13)
            rightDistance = reading(0, 16, 18)
            leftDistance = reading(0, 29, 31)
            print("read ultrasonic distance ... {} {} {}".format(frontDistance, rightDistance, leftDistance))

            if frontDistance <= 18:
                if rightDistance < leftDistance and rightDistance <= 10:
                    print("go left")
                    left.moveToLeft()

                elif leftDistance < rightDistance and leftDistance <= 10:
                    print("go right")
                    right.moveToRight()

                else:
                    print("de back")
                    back.goBack()

            elif frontDistance >= 18 and rightDistance >= 12 and leftDistance>= 10:
                print("go right2")
                #right45.moveToRight45()
                right45.test()

            elif frontDistance >= 18 and rightDistance >= 10 and leftDistance>= 12:
                print("go left2")
                left45.moveToLeft45()

            elif frontDistance >= 18 and rightDistance >= 12 and leftDistance>= 12:
                print("go straight")
                straight.moveToStraight()

            elif rightDistance <= leftDistance and rightDistance <= 10:
                print("change direction to left")
                left.moveToLeft()

            elif leftDistance <= rightDistance and leftDistance <= 10:
                print("change direction to right")
                right.moveToRight()

            pass

    except KeyboardInterrupt:
        print("foo")
        stop.stop()

if __name__ == "__main__":
    control()
