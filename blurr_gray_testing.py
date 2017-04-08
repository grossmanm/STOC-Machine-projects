import cv2
import numpy as np
cv2.namedWindow("Blurr & Grayscale testing")
cam = cv2.VideoCapture(0)
if cam.isOpened():
    ret, frame = cam.read()
else:
    ret = False
while(True):
    ret, frame = cam.read()
    img = cv2.bilateralFilter(frame, 15, 75, 75)
    imgg = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY )
    imggg = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # I tried so hard and got so far, but in the end I am just the smoking man from X-files
    cv2.imshow("Blur Testing", img)
    #cv2.imshow("No Blur", frame)
    cv2.imshow("W/ Alpha Channel", imgg)
    cv2.imshow("No Alpha Channel", imggg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
