import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\ASUS\\MACHINE LEARNING AND DATA SCIENCE\OPENCV\\videos\\VN20230427_233342.mp4")
ret,frame=cap.read()
count =0

while (True):
    # ret, frame = cap.read()
    # count=0
    if ret is True:
        cv2.imwrite('videos\\frames\\img%d.jpg'%count,frame)
        cap.set(cv2.CAP_PROP_POS_MSEC, count*1000)
        ret,frame=cap.read()
        frame=cv2.resize(frame,(int(cap.get(3)),int(cap.get(4))))
        cv2.imshow('frame', frame)
        count +=1
        k=cv2.waitKey(1)
        print(count)
        if k==ord('q')&0xFF:
            break
            # cv2.destroyAllWindows()
cap.release()
cv2.destroyAllWindows()