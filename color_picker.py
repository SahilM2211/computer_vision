import cv2
import numpy as np

def empty(x):
    pass

img=np.zeros((200,512,3),np.uint8)
cv2.namedWindow("color_picker")

#create a switch

s="0:off\n1:on"
cv2.createTrackbar(s,"color_picker",0,1,empty)
cv2.createTrackbar("r","color_picker",0,255,empty)
cv2.createTrackbar("g","color_picker",0,255,empty)
cv2.createTrackbar("b","color_picker",0,255,empty)

while True:
    cv2.imshow("color_picker",img)
    k=cv2.waitKey(1)
    if k==ord('q')&0xff:
        break

    s1=cv2.getTrackbarPos(s,"color_picker")
    R=cv2.getTrackbarPos("r","color_picker")
    G=cv2.getTrackbarPos("g","color_picker")
    B=cv2.getTrackbarPos("b","color_picker")

    if s1==0:
        img[:]=0
    else:
        img[:]=[R,G,B]

cv2.destroyAllWindows()

