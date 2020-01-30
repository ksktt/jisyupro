import cv2
import numpy as np

import sys
sys.path.append('..')

#import straight
#import rotation
#from omni import straight

from image_processing import NaiveTTC


if __name__=="__main__":
    WIDTH = 64
    HEIGHT = 48
    FRAMERATE = 30

    INITIAL = 0.5*FRAMERATE #step number after start
    KEEP_BRAKE = 0.2*FRAMERATE #step number
    THRESHOLD = 0.45 #stop when assuming TTC is under this threshold
    R = 0.4 #renewal ration of assuming TTC

    #cap = cv2.VideoCapture("rpicamsrc rotation=180 ! video/x-raw,format=I420,width={},height={},framerate={}/1 ! appsink".format(WIDTH,HEIGHT,FRAMERATE))
    cap = cv2.VideoCapture(0)

    #init
    ret,raw = cap.read()
    if not ret:
        print("cannot connect to camera ")
        exit()

    img = raw[:HEIGHT].astype(np.float32) # I420->Y
    ettc = NaiveTTC(img,FRAMERATE,m0=5,r0=0.60)

    #straight.moveToStraight()
    brake = 0
    mttc = 0.50
    for i in range(10*FRAMERATE):
        ret,raw = cap.read()
        img = raw[:HEIGHT].astype(np.float32) # I420->Y

        ttc = ettc.update(img)
        if ttc>0:
            mttc = min(1.0,(1-R)*mttc+R*ttc)

        print("{0:+03.6f}".format(mttc))

        if INITIAL<i and brake==0 and mttc<THRESHOLD:
            brake = 1
        if brake>0:
            if brake<KEEP_BRAKE:
                brake += 1
            else:
                break
        print("now braking ... {}".format(brake))

    #rotation.rotation()
