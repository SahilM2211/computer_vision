import cv2
import pyautogui as py
import numpy as np

rs=py.size()
path=input("enter filename and path")
fps=20.0
fourcc=cv2.VideoWriter_fourcc(*"mp4v")
output=cv2.VideoWriter(path,fourcc,fps,rs)

cv2.namedWindow("live_recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow('live_recording',(720,480))

while True:
    img=py.screenshot()
    frame=np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output.write(frame)
    cv2.imshow("live_recording", frame)
    k=cv2.waitKey(1)
    if k==ord('q')&0xFF:
        break
output.release()
cv2.destroyAllWindows()