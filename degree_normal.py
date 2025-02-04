
import random
import cv2
import math

import numpy as np
 
path = 'Screenshot_21.png'
img = cv2.imread(path)
pointsList = []


def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            cv2.line(img,tuple(pointsList[round(size-1)]),(x,y),(0,0,255),2)
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointsList.append([x,y])
 
def gradient(pt1,pt2):
    try:
        return (pt2[1]-pt1[1]) / (pt2[0]-pt1[0]+1e-10)

    except ZeroDivisionError:
        return 0
 
def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    m1 = gradient(pt1,pt2)
    print(m1)
    m2 = gradient(pt2,pt3)
    print(m2)
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR), 4)

    cv2.putText(img,str(angD),(pt2[0]+30,pt2[1]-20),cv2.FONT_HERSHEY_SIMPLEX,.5,(0,0,0),2) 
while True:
    if len(pointsList) % 3 == 0 and len(pointsList) !=0:
        getAngle(pointsList)
 
    cv2.imshow('Image',img)
    cv2.setMouseCallback('Image',mousePoints)
    # press q untuk hapus
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        img = cv2.imread(path)
    # press w untuk keluar
    elif cv2.waitKey(1) & 0xFF == ord('w'):
        cv2.destroyAllWindows()
        break