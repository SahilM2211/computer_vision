import cv2
import numpy as np

img = cv2.imread("images\\tancent2.png")
img=cv2.resize(img,(400,400))
print("shape:",img.shape)#(width,height,and color channel)of image
print("size:",img.size)#no. of pixels in images
print("dtype:",img.dtype)#dtype of array(uint8)
print("imagetype",type(img))#type of image(array)
px=img[200,200]#pixel value in arrey
print(px)#for particular pixel
b=img[200,200,0]#pixel value and color channel value
print("blue:",b)
g=img[200,200,1]
print("green:",g)
r=img[200,200,2]
print("red:",r)

b,g,r=cv2.split(img)#split image in color channel
print(b,g,r)

merge_img=cv2.merge((r,b,g))#merge image via image channel
merge_img1=cv2.merge((b,r,g))
merge_img2=cv2.merge((g,b,r))
merge_img3=cv2.merge((g,r,b))


# cv2.imshow('merge',merge_img)
# cv2.imshow('merge1',merge_img1)
# cv2.imshow('merge2',merge_img2)
# cv2.imshow('merge3',merge_img3)
# cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

