import cv2
import numpy as np

img=cv2.imread('images\\download.jpg')
img=cv2.resize(img,(720,480))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,mask=cv2.threshold(gray,27,255,cv2.THRESH_BINARY)

kernel=np.ones((3,3),np.uint8)
erosion=cv2.erode(mask,kernel)

dialation=cv2.dilate(mask,kernel)

cv2.imshow('erosion',erosion)
cv2.imshow('dialation',dialation)
cv2.imshow('input',img)
cv2.imshow('mask',mask)
# cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()