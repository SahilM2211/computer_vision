import cv2
import numpy as np

img=cv2.imread('images\\tancent2.png')
#cv2.copyMakeBorder(maintimage,top,bottom,right,left,bordertype,value=[colorcode_value])
#this function use for make border on image
#top,bottom,right,left is thickness of the border
img=cv2.copyMakeBorder(img,10,10,5,5,cv2.BORDER_CONSTANT,value=[200,0,100])
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()