import cv2
import numpy as np

img_1=cv2.imread('images\\sahil_1.jpg')
img_2=cv2.imread('images\\tansent1.png')

img_1=cv2.resize(img_1,(720,480))
img_2=cv2.resize(img_2,(400,480))

r,c,ch=img_2.shape
print(r,c,ch)

roi=img_1[0:r,0:c]

gray_2=cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)

mask=cv2.adaptiveThreshold(gray_2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,20)

mask_inv=cv2.bitwise_not(mask)

img_1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)

img_2_fg=cv2.bitwise_and(img_2,img_2,mask=mask)

res=cv2.addWeighted(img_1_bg,0,img_2_fg,1,0)

# cv2.imshow('img_1',img_1)
# cv2.imshow('img_2',img_2)
# cv2.imshow('roi',roi)
cv2.imshow('thresholding',mask)
# cv2.imshow('thresholding_inv',mask_inv)
# cv2.imshow('img_1_bg',img_1_bg)
# cv2.imshow('img_2_fg',img_2_fg)
cv2.imshow('res',res)

final=img_1
final[0:r,0:c]=res
cv2.imshow('final',final)
cv2.waitKey(0)
cv2.destroyAllWindows()