#bitwise operations includes and,or, not,xor operations
#it is most important  and use ofr various purpose like masking
#and find roi(region of interest)  which is in complex shape
import cv2
import numpy as np

img1=np.zeros([500,500,3],np.uint8)
img1=cv2.rectangle(img1,(100,250),(30,130),[255,255,255],-1)

img2=np.zeros([500,500,3],np.uint8)
img2=cv2.rectangle(img2,(150,300),(40,90),[255,255,255],-1)

#bitwise_and operation
# bitwise_and=cv2.bitwise_and(img1,img2)

#bitwise_or operation
# bitwise_or=cv2.bitwise_or(img1,img2)

#bitwise_not operation
# bitwise_not_x=cv2.bitwise_not(img1)
# bitwise_not_y=cv2.bitwise_not(img2)

#bitwise_xor operation
bitwise_xor=cv2.bitwise_xor(img1,img2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
# cv2.imshow('bitwise_and',bitwise_and)
# cv2.imshow('bitwise_or',bitwise_or)
# cv2.imshow('bitwise_not_x',bitwise_not_x)
# cv2.imshow('bitwise_not_y',bitwise_not_y)
cv2.imshow('bitwise_xor',bitwise_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()