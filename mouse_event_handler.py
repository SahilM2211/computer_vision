# import cv2
# import numpy as np
#
# def draw(event,x,y,flags,params):
#
#     try:
#         if event== cv2.EVENT_LBUTTONDBLCLK:
#             cv2.circle(img,(x,y),10,(100,200,255),2)
#         elif event== cv2.EVENT_RBUTTONDBLCLK:
#             cv2.rectangle(img,(x,y),(x+55,y+86),(200,100,255),2)
#         print("x:",x)
#         print("y:",y)
#         print("flags:",flags)
#         print('params:',params)
#     except Exception as e:
#         print("error occured")
#
# cv2.namedWindow(winname='result')
# img=np.zeros((512,512,4),np.uint8)
# cv2.setMouseCallback("result",draw)
#
# while True:
#     cv2.imshow("result",img)
#     k=cv2.waitKey(0)
#     if k==ord('q')&0xff:
#         break
# cv2.destroyAllWindows()

# import cv2
# import numpy as  np
#
# def draw(event,x,y,flags,params):
#
#             font=cv2.FONT_HERSHEY_PLAIN
#             if event==cv2.EVENT_LBUTTONDOWN:
#                 print(x,",",y)
#                 cord="."+str(x)+","+str(y)
#                 cv2.putText(img,cord,(x,y),font,1,(100,200,255),2)
#             elif event==cv2.EVENT_RBUTTONDOWN:
#                 a=img[y,x,0]
#                 b=img[y,x,1]
#                 c=img[y,x,2]
#                 text="."+str(a)+","+str(b)+","+str(c)
#                 cv2.putText(img, text, (x, y), font, 1, (200, 100, 255), 2)
#
#
# cv2.namedWindow(winname='res')
# # img=np.zeros((512,512,3),np.uint8)
# img=cv2.imread('images\\tancent2.png')
# cv2.setMouseCallback("res",draw)
#
# while True:
#     cv2.imshow("res",img)
#     k=cv2.waitKey(0)
#     if k==ord('q')&0xff:
#         break
# cv2.destroyAllWindows()
