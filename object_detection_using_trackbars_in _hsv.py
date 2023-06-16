# import cv2
# import numpy as np
#
# img=cv2.imread('images\\download.jpg')
# def empty(x):
#     pass
# cv2.namedWindow('color_adjustments')
# cv2.createTrackbar('LOWER_H','color_adjustments',0,255,empty)
# cv2.createTrackbar('LOWER_S','color_adjustments',0,255,empty)
# cv2.createTrackbar('LOWER_V','color_adjustments',0,255,empty)
# cv2.createTrackbar('UPPER_H','color_adjustments',255,255,empty)
# cv2.createTrackbar('UPPER_S','color_adjustments',255,255,empty)
# cv2.createTrackbar('UPPER_V','color_adjustments',255,255,empty)
# while True:
#    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#    L_H=cv2.getTrackbarPos('LOWER_H','color_adjustments')
#    L_S=cv2.getTrackbarPos('LOWER_S','color_adjustments')
#    L_V=cv2.getTrackbarPos('LOWER_V','color_adjustments')
#    U_H=cv2.getTrackbarPos('UPPER_H','color_adjustments')
#    U_S=cv2.getTrackbarPos('UPPER_S','color_adjustments')
#    U_V=cv2.getTrackbarPos('UPPER_V','color_adjustments')
#
#    lower_bound=np.array([L_H,L_V,L_V])
#    upper_bound=np.array([U_H,U_V,U_V])
#
#    mask=cv2.inRange(hsv,lower_bound,upper_bound)
#    bitwise_and=cv2.bitwise_and(img,img,mask=mask)
#
#    cv2.imshow('img',img)
#    cv2.imshow('mask',mask)
#    cv2.imshow('bitwise_and',bitwise_and)
#    k=cv2.waitKey(1)
#    if k==ord('q'):
#        break
# cv2.destroyAllWindows()

# same task for webcam video
import cv2
import numpy as np

cap=cv2.VideoCapture(0)

def empty(x):
    pass
cv2.namedWindow('color_adjustments')
cv2.createTrackbar('LOWER_H','color_adjustments',0,255,empty)
cv2.createTrackbar('LOWER_S','color_adjustments',0,255,empty)
cv2.createTrackbar('LOWER_V','color_adjustments',0,255,empty)
cv2.createTrackbar('UPPER_H','color_adjustments',255,255,empty)
cv2.createTrackbar('UPPER_S','color_adjustments',255,255,empty)
cv2.createTrackbar('UPPER_V','color_adjustments',255,255,empty)
while True:
   ret,frame=cap.read()
   frame=cv2.resize(frame,(400,400))
   hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   L_H=cv2.getTrackbarPos('LOWER_H','color_adjustments')
   L_S=cv2.getTrackbarPos('LOWER_S','color_adjustments')
   L_V=cv2.getTrackbarPos('LOWER_V','color_adjustments')
   U_H=cv2.getTrackbarPos('UPPER_H','color_adjustments')
   U_S=cv2.getTrackbarPos('UPPER_S','color_adjustments')
   U_V=cv2.getTrackbarPos('UPPER_V','color_adjustments')

   lower_bound=np.array([L_H,L_V,L_V])
   upper_bound=np.array([U_H,U_V,U_V])

   mask=cv2.inRange(hsv,lower_bound,upper_bound)
   bitwise_and=cv2.bitwise_and(frame,frame,mask=mask)

   cv2.imshow('frame',frame)
   cv2.imshow('mask',mask)
   cv2.imshow('bitwise_and',bitwise_and)
   k=cv2.waitKey(1)
   if k==ord('q'):
       break
cv2.destroyAllWindows()