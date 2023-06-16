#cornerHarris detection
#cv2.cornerHarris(gray_img,write_img,blocksize,ksize,freeparameter,border_type or thickness)
import cv2
import numpy as np
# img=cv2.imread('images\\arjun.jpg')
# img1=cv2.imread('images\\arjun.jpg')
# img=cv2.resize(img,(720,720))
# img1=cv2.resize(img1,(720,720))
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray=cv2.cornerHarris(gray,2,3,0.04)
# gray=cv2.dilate(gray,None, iterations=1)
# img[gray>0.01*gray.max()]=[0,0,255]
# cv2.imshow('output',img)
# cv2.imshow('input',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#shi_tomasi_corner_datection
#cv2.goodFeaturesToTrack(gray_img,max no.of corners,quality parameter(preferred=0.01),minimum_ditance(preferred=10)
# img=cv2.imread('images\\arjun.jpg')
# img1=cv2.imread('images\\arjun.jpg')
# img=cv2.resize(img,(720,720))
# img1=cv2.resize(img1,(720,720))
#
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# output=cv2.goodFeaturesToTrack(gray,100,0.01,10)
# output=np.int0(output)
# print(output)
# for i in output:
#     x,y=i.ravel()
#     print(x,y)
#     cv2.circle(img,(x,y),3,[0,0,255],-1)
# cv2.imshow('output',img)
# cv2.imshow('input',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#SIFT(scale invarient feature transform)
#this method use for detect corner,blobs and circles from image
#this method is more efficienty compare to shi tomashi and corner_harris

img=cv2.imread('images\\arjun.jpg')
img1=cv2.imread('images\\arjun.jpg')
img=cv2.resize(img,(720,720))
img1=cv2.resize(img1,(720,720))

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
output=cv2.SIFT_create()
kp,des=output.detectAndCompute(gray,None)
img=cv2.drawKeypoints(img,kp,None,[0,255,0])
cv2.imshow('output',img)
cv2.imshow('input',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


#FAST(Features from accelerated segment test )
#this is corner detection method
# img=cv2.imread('images\\arjun.jpg')
# img1=cv2.imread('images\\arjun.jpg')
# img=cv2.resize(img,(720,720))
# img1=cv2.resize(img1,(720,720))
#
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # Create FAST detector object
# fast = cv2.FastFeatureDetector_create(threshold=30, nonmaxSuppression=True)
#
# # Detect keypoints
# keypoints = fast.detect(gray, None)
#
# # Draw keypoints on the original image
# img = cv2.drawKeypoints(img, keypoints, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#
#
# cv2.imshow('output',img)
# cv2.imshow('input',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#BRIEF(Binary Robust Independent Elementary Features)
'''The major function of BRIEF is to identify the patches around the keypoint
 and convert them into a binary vector, so that they can represent an object.'''


