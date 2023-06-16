'''image blending is a method of put one image channel in another image
in sort add two image in one and create a new image or add one image in another image'''
"blending means addition of two images"
"if you want to blend two images than they must have in same size"
'cv2.add(),and cv2.addWeighted() we use for image blending'


import cv2
import numpy as np

img1= cv2.imread('C:\\Users\\ASUS\\MACHINE LEARNING AND DATA SCIENCE\\OPENCV\images\\download.jpg')
img1=cv2.resize(img1,(720,720))
img2=cv2.imread('C:\\Users\\ASUS\\MACHINE LEARNING AND DATA SCIENCE\\OPENCV\\images\\sahil.jpg')
img2=cv2.resize(img2,(720,720))
# img3=cv2.imread('images\\tancent2.png')
# img3=cv2.resize(img3,(720,720))
#add array of one image in another image
# result=img1+img2
# cv2.imshow('result',result)
'''in upper method we add one image array value in another in another iamge
but we get in output some damage pixels this method is not a blending method 
we need to use opencv blending function like cv2.add(), cv2.addWeighted() function'''
#cv2.add() function implementation
# result1=cv2.add(img1,img2)
# cv2.imshow('result1',result1)
'''upper funtion cv2.add() blend image in same weight and 
you can give any image first and second no numbervise require
it will give same output for any numbering'''
#cv2.addweighted(img1,color_saturation,img2,color_saturation,gamma_value)
result2=cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('result2',result2)
'''in uppper function takes five parameter as an input image 1,
saturation_value,image2,saturation_value,gamma value
saturation_value sum must be 1,it takes max 2 image as input.'''
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()