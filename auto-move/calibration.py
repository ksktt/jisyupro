##ref: http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html
import numpy as np
import cv2
import glob

width = 800
height = 600

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
##ref: https://stackoverflow.com/questions/39272510/camera-calibration-with-circular-pattern
objp=np.array([[0,0,0],[1,0,0],[2,0,0],[3,0,0],[0.5,0.5,0],[1.5,0.5,0],[2.5,0.5,0],[3.5,0.5,0]])
for y in range(2,11):
        for x in range(4):
                objp=np.append(objp,[np.array([objp[4*(y-2)+x][0],objp[4*(y-2)+x][1]+1,0])],axis=0)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('c*.jpg')
print(images)
for fname in images:
    img = cv2.imread(fname)
    img = cv2.resize(img,(width,height))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findCirclesGrid(gray, (4,11),flags=cv2.CALIB_CB_ASYMMETRIC_GRID+cv2.CALIB_CB_CLUSTERING)
    print(ret)
    # If found, add object points, image points (after refining them)
    if ret == True:
        corners2 = cv2.cornerSubPix(gray,corners,(4,11),(-1,-1),criteria)
        imgpoints.append(corners2.reshape((1,-1,2)))

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (4,11), corners2,ret)

        cv2.imshow('img',img)
        cv2.waitKey(100)


objpoints = [objp.astype(np.float32).reshape((1,-1,3))]*len(imgpoints)

##projection
# ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

##fisheye
##ref: https://bitbucket.org/amitibo/pyfisheye/src
K = np.zeros((3,3),dtype=np.float32)
D = np.zeros((4, 1),dtype= np.float32)
rvecs = [np.zeros((1, 1, 3), dtype=np.float32)]*len(imgpoints)
tvecs = [np.zeros((1, 1, 3), dtype=np.float32)]*len(imgpoints)
rms, _, _, _, _ = cv2.fisheye.calibrate(
    objpoints,imgpoints,(width,height),
    K,D,rvecs,tvecs,
    cv2.fisheye.CALIB_RECOMPUTE_EXTRINSIC+cv2.fisheye.CALIB_FIX_SKEW)

print(rms)
print(K)
print(D)

np.save("K.npy",K)
np.save("D.npy",D)

##display
for fname in images:
    img = cv2.imread(fname)
    img = cv2.resize(img,(width,height))

    ##projection
    # newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(width,height),1,(width,height))
    # dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

    ##fisheye
    newcameramtx = cv2.fisheye.estimateNewCameraMatrixForUndistortRectify(K,D,(width//2,height//2),np.eye(3))
    dst = cv2.fisheye.undistortImage(img, K, D, Knew=newcameramtx)

    cv2.imshow("dst",dst)
    cv2.waitKey()

cv2.destroyAllWindows()
