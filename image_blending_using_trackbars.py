import cv2
import numpy as np
img1=cv2.imread('C:\\Users\\ASUS\\MACHINE LEARNING AND DATA SCIENCE\\OPENCV\images\\arjun.jpg')
img1=cv2.resize(img1,(720,720))
img2=cv2.imread('images\\group.jpg')
img2=cv2.resize(img2,(720,720))
def blend(x):
    pass
img=np.zeros([500,500,3],np.uint8)
cv2.namedWindow('win')
cv2.createTrackbar('alpha',"win",0,100,blend)
s="0:off\n1:on"
cv2.createTrackbar(s,"win",0,1,blend)
# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)
while True:
    s1=cv2.getTrackbarPos(s,"win")
    a=cv2.getTrackbarPos("alpha","win")
    n=float(a/100)
    print(n)

    if s1==0:
        dst=img[:]
    else:
        dst=cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dst,str(a),(20,50),cv2.FONT_ITALIC,2,(0,115,225),2)
    cv2.imshow("dst", dst)
    k = cv2.waitKey(1)
    if k == ord('q') & 0xff:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()