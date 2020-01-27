import cv2
import numpy as np
import math

#from image_processing import InverseTTCMap
from image_processing import NaiveTTC
#from car_controller import CarController

import straight
import stop
import rotation
import steering

if __name__=="__main__":
    import time

    WIDTH = 64
    HEIGHT = 48
    Y0 = 24
    Y1 = HEIGHT-2
    FRAMERATE = 30

    M0 = 6
    ITTC0 = 0.0

    LOSS_BINS = 16
    LOSS_SIGMA = LOSS_BINS*0.4
    LOSS_CAP = 10

    STEER_R = 0.6
    STEER_K = 3.0

    BRAKE_W = 6
    BRAKE_R = 0.5
    BRAKE_THRESH = 4.0

    #ctrl = CarController()
    cap = cv2.VideoCapture(0)

    ret, raw = cap.read()

    #Initialize estimator
    #estimator = InverseTTCMap(WIDTH,HEIGHT-Y0,FRAMERATE,threshold=ITTC0,m0=M0,y0=Y0)img = raw[:HEIGHT].astype(np.float32) # I420->Y
    img = raw[:HEIGHT].astype(np.float32) # I420->Y
    estimator = NaiveTTC(img,FRAMERATE,m0=5,r0=0.60)

    #strart moving
    straight.moveToStraight()

    for i in range(FRAMERATE//2):
        cap.grab()

    ##main loop
    mean_steer = 0
    mean_loss = 0
    for i in range(FRAMERATE*10):
        #capture
        ret,raw = cap.read()
        img = raw[Y0:Y1].astype(np.float32) # I420->Y

        #estimate before collision

        if i==0:
            img = raw[:HEIGHT].astype(np.float32) # I420->Y
            continue

        ittcmap = estimator.update(img)

        #post processing
        ittcmap = cv2.dilate(ittcmap,np.ones((3,3)))
        loss = cv2.resize(ittcmap,(LOSS_BINS,1),cv2.INTER_AREA)
        area = cv2.resize(1.0*(ittcmap>ITTC0),(LOSS_BINS,1),cv2.INTER_AREA)
        loss = loss/(area+1e-3)
        #smoothing
        loss = np.minimum(loss,LOSS_CAP)
        loss = cv2.GaussianBlur(loss,(LOSS_BINS+1,1),LOSS_SIGMA)
        loss = loss.flatten()[2:-2] # 画面端はうまくスムージングできないので使わない

        imin = np.argmin(loss)

        #steering
        if loss[imin]<=0:
            steer = 0.0
        else:
            steer = 2*imin/(len(loss)-1)-1.0 # NOTE: -1 <= steer <= 1
            steer *= math.pow(abs(steer),0.5)
        mean_steer = (1-STEER_R)*mean_steer+STEER_R*steer
        steering.direction(STEER_K*mean_steer)

        #move slowly before obstacle
        w = BRAKE_W//2
        imin = max(w,min(len(loss-w-1),imin))
        loss = loss[imin-w:imin+w+1]
        #average
        positive_loss = loss[loss>0]
        if len(positive_loss)>0:
            mean_loss = (1-BRAKE_R)*mean_loss+BRAKE_R*np.mean(positive_loss)
        if mean_loss>BRAKE_THRESH:
            straight.moveSlowly()
            break

    stop.stop()
