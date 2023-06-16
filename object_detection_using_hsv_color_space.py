import cv2
import numpy as np

img=cv2.imread('images\\download.jpg')
while True:
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    u_v=np.array([48,255,248])
    l_v=np.array([20,143,139])
    mask=cv2.inRange(hsv,l_v,u_v)#first give image,than lower value,and then after upper value.
    bitwise_and=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('bitwise_and',bitwise_and)
    cv2.imshow('img',img)
    cv2.imshow('mask',mask)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cv2.destroyAllWindows()
