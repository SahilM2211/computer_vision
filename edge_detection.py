#canny edge detction

import cv2
import numpy as np

# cap=cv2.VideoCapture(0)
# while cap.isOpened():
#     ret,frame=cap.read()
#     if ret is True:
#         frame = cv2.resize(frame, (720,480))
#         gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         canny_edge=cv2.Canny(gray,100,200)
#         cv2.imshow('canny_edge',canny_edge)
#         k=cv2.waitKey(1)
#         if k==ord('q')&0xff:
#             break
# cap.release()
# cv2.destroyAllWindows()

# img_1=cv2.imread('C:\\Users\\ASUS\\MACHINE LEARNING AND DATA SCIENCE\\OPENCV\\images\\tansent1.png')
# img_2=cv2.imread('C:\\Users\\ASUS\\MACHINE LEARNING AND DATA SCIENCE\\OPENCV\\images\\tancent2.png')
#
# img_1=cv2.resize(img_1,(720,480))
# img_2=cv2.resize(img_2,(720,480))
#
# gray_1=cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
# gray_2=cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)
#
# edge_1=cv2.Canny(gray_1,100,200)
# edge_2=cv2.Canny(gray_2,100,200)
#
# cv2.imshow('img_1',edge_1)
# cv2.imshow('img_2',edge_2)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

