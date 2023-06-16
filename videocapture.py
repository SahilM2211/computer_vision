# import cv2
#video play from local disk
# cap=cv2.VideoCapture(r"C:\\Users\\ASUS\Desktop\\[Allmovieshub.vip]-Phir Hera Pheri 2006 WebRip Hindi 480p ESub - .mkv")
# print("cap",cap)
# while (True):
#     ret,frame = cap.read()
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     frame = cv2.resize(frame,(720,480),interpolation=cv2.INTER_AREA)
#     cv2.imshow('GRAY', gray)
#     cv2.imshow('output',frame)
#     k=cv2.waitKey(25)
#     if k==ord('9')& 0xFF:
#         break
# cap.release()
# cv2.destroyAllWindows()

#video capture from webcam and save it
# import cv2
#
# cap=cv2.VideoCapture(0)
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# OUTPUT=cv2.VideoWriter('output.avi',fourcc,20,(int(cap.get(3)), int(cap.get(4))),0)
# while cap.isOpened():
#     ret,frame = cap.read()
#     if ret is True:
#         gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         # frame = cv2.resize(frame,(1280,1080),interpolation=cv2.INTER_AREA)
#         cv2.imshow('GRAY', gray)
#         # cv2.imshow('output',frame)
#         OUTPUT.write(gray)
#         k=cv2.waitKey(1)
#         if k & 0xFF ==ord('9'):
#             break
# cap.release()
# OUTPUT.release()
# cv2.destroyAllWindows()

##video capture from mobile camera
# import cv2
# camera='http://25.75.244.122:8080/video'
# cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cap.open(camera)
# fourcc=cv2.VideoWriter_fourcc(*'mp4v')
# OUTPUT=cv2.VideoWriter('output.mp4',fourcc,20,(int(cap.get(3)), int(cap.get(4))),0)
# while cap.isOpened():
#     ret,frame = cap.read()
#     if ret is True:
#         gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         # frame = cv2.resize(frame,(720,480),interpolation=cv2.INTER_AREA)
#         cv2.imshow('GRAY', gray)
#         # cv2.imshow('output',frame)
#         OUTPUT.write(gray)
#         k=cv2.waitKey(1)
#         if k & 0xFF ==ord('9'):
#             break
# cap.release()
# OUTPUT.release()
# cv2.destroyAllWindows()


#youtube video play
import cv2
import pafy
import youtube_dl
url="https://www.youtube.com/watch?v=VsuGZJybKso"
data=pafy.new(url)
data=data.getbest(preftype='mp4')
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url)
# fourcc=cv2.VideoWriter_fourcc(*'mp4v')
# OUTPUT=cv2.VideoWriter('output.mp4',fourcc,20,(int(cap.get(3)), int(cap.get(4))),0)
while cap.isOpened():
    ret,frame = cap.read()
    if ret is True:
        frame = cv2.resize(frame,(720,480),interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('GRAY', gray)
        cv2.imshow('output',frame)
        # OUTPUT.write(gray)
        k=cv2.waitKey(1)
        if k & 0xFF ==ord('9'):
            break
cap.release()
# OUTPUT.release()
cv2.destroyAllWindows()

