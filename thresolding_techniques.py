import cv2
import numpy as np
#
# cap=cv2.VideoCapture(0)
#
# while cap.isOpened():
#     ret,frame = cap.read()
#     if ret is True:
#         frame = cv2.resize(frame,(400,400))
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         # _,thresh_1=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#         # _,thresh_2=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
#         # _,thresh_3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
#         # _,thresh_4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
#         # _,thresh_5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
#         # thresh_6=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#         # thresh_7=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#         # _,thresh_8=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#         _,thresh_9=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#         blur = cv2.GaussianBlur(gray, (5, 5), 0)
#         _,thresh_10=cv2.threshold(blur,0,255,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
#         # cv2.imshow('binary',thresh_1)
#         # cv2.imshow('binary_inv',thresh_2)
#         # cv2.imshow( 'trunc',thresh_3)
#         # cv2.imshow( 'tozero',thresh_4)
#         # cv2.imshow( 'tozero_inv',thresh_5)
#         # cv2.imshow('adaptive_thresh_mean_c', thresh_6)
#         # cv2.imshow('adaptive_thresh_gaussian_c', thresh_7)
#         # cv2.imshow('otsu+binary', thresh_8)
#         cv2.imshow('otsu+binary_inv', thresh_9)
#         cv2.imshow('otsu+tozero', thresh_10)
#         k=cv2.waitKey(1)
#         if k & 0xFF ==ord('9'):
#             break
#
#
# cap.release()
# cv2.destroyAllWindows()

#for image

img_1=cv2.imread('C:\\Users\\ASUS\\MACHINE LEARNING AND DATA SCIENCE\\OPENCV\\images\\tansent1.png')
img_2=cv2.imread('C:\\Users\\ASUS\\MACHINE LEARNING AND DATA SCIENCE\\OPENCV\\images\\tancent2.png')
img_3=cv2.imread('C:\\Users\\ASUS\\MACHINE LEARNING AND DATA SCIENCE\\OPENCV\\images\\tansent.png')

img_1=cv2.resize(img_1,(720,480))
img_2=cv2.resize(img_2,(720,480))
img_3=cv2.resize(img_3,(720,480))

gray_1=cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
gray_2=cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)
gray_3=cv2.cvtColor(img_3,cv2.COLOR_BGR2GRAY)

# _,thresh_1=cv2.threshold(gray_1,90,255,cv2.THRESH_BINARY)
# _,thresh_2=cv2.threshold(gray_1,127,255,cv2.THRESH_BINARY_INV)
# _,thresh_3 = cv2.threshold(gray_1, 90, 255, cv2.THRESH_TRUNC)
# _,thresh_4 = cv2.threshold(img_1, 90, 255, cv2.THRESH_TOZERO)
# _,thresh_5 = cv2.threshold(gray_1, 127, 255, cv2.THRESH_TOZERO_INV)
#blocksize always in odd number and grater than 1 like 3,5,7 etc.
# thresh_6=cv2.adaptiveThreshold(gray_1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# thresh_7=cv2.adaptiveThreshold(gray_1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# _,thresh_8=cv2.threshold(gray_1,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# _,thresh_9=cv2.threshold(gray_1,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# blur = cv2.GaussianBlur(gray_1, (5, 5), 0)
_,thresh_10=cv2.threshold(gray_1,00,255,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
_,thresh_11=cv2.threshold(gray_1,60,255,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)

# cv2.imshow('binary',thresh_1)
# cv2.imshow('binary_inv',thresh_2)
# cv2.imshow( 'trunc',thresh_3)
# cv2.imshow( 'tozero',thresh_4)
# cv2.imshow( 'tozero_inv',thresh_5)
# cv2.imshow('adaptive_thresh_mean_c', thresh_6)
# cv2.imshow('adaptive_thresh_gaussian_c', thresh_7)
# cv2.imshow('otsu+binary', thresh_8)
# cv2.imshow('otsu+binary_inv', thresh_9)
cv2.imshow('otsu+tozero', thresh_10)
cv2.imshow('otsu+trunc', thresh_11)
cv2.imshow('img_1',img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()




