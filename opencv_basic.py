# import numpy as np
# import cv2
#
# img = cv2.imread('images\\tancent2.png')
# print(img.shape)
# #draw line on image
# img=cv2.line(img,(0,0),(200,100),(92,67,73),3)#cv2.line(image,start_point(x1,x2),end_point(y1,y2),colorcode in bgr,thickness)
# #draw rectengle on image
# img=cv2.rectangle(img,(200,50),(30,80),(145,89,76),3)#cv2.rectangle(image,start_point(x1,x2),end_point(y1,y2),colorcode in bgr,thickness)
# #draw arrowed line on image
# img=cv2.arrowedLine(img,(90,76),(300,250),(57,189,255),3)#cv2.arrowedLine(image,start_point(x1,x2),end_point(y1,y2),colorcode in bgr,thickness)
# #draw circle on image
# img=cv2.circle(img,(98,99),99,(75,130,222),3)#cv2.circle(image,start_point(x1,x2),radius,colorcode in bgr,thickness)
# #draw ellipse on image
# img=cv2.ellipse(img,(98,170),(23,76),0,0,270,155,3)#cv2.ellipse(image,start_point(x1,x2),(length,height),tilt points suggest value 0 ,tilt points suggest value 0,angle,colorcode in bgr,thickness)
# #draw text on image
# font=cv2.FONT_HERSHEY_COMPLEX
# img=cv2.putText(img,'Tensent',(250,225),font,3,(0,0,0),3,cv2.LINE_AA)#cv2.putText(image,text,start_point(x1,x2),font,fontsize,colorcode in bgr,thickness,linetype)
# #create black image
# img=np.zeros([234,353,3],np.uint8)*255
# #create white image
# img=np.ones([234,353,3],np.uint8)*255
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # resize = cv2.resize(gray, (1280, 720), interpolation=cv2.INTER_LINEAR)
# # kernel = np.ones((5, 5), np.uint8)
# # erosion = cv2.dilate(gray, kernel, iterations=1)
# cv2.imshow('output',img)
# # cv2.imshow("o", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#same on video
import cv2
import datetime

cap=cv2.VideoCapture("videos\\Marvel Studios' Avengers： Infinity War Official Trailer.mp4")
print("width",str(cap.get(3)))
print("height",str(cap.get(4)))
while cap.isOpened():
    ret,frame=cap.read()
    if ret is True:
        text='width: ' + str(cap.get(3))+ ' height: '+str(cap.get(4))
        font=cv2.FONT_HERSHEY_COMPLEX_SMALL
        frame=cv2.putText(frame,text,(675,67),font,1,(234,76,45),3,cv2.LINE_AA)
        data=str(datetime.datetime.now())
        frame=cv2.putText(frame,data,(129,67),font,1,(240,76,244),3,cv2.LINE_AA)

        cv2.imshow('avenger',frame)
        k =cv2.waitKey(25)
        if k ==ord('q')&0xFF:
            break
cap.release()
cv2.destroyAllWindows()


