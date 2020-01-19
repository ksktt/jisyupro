import cv2

cap_cam = cv2.VideoCapture(0)
print(type(cap_cam))

print(cap_cam.isOpened())
