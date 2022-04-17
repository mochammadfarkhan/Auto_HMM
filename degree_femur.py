
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
        if size != 0 and size % 2 != 0:
            cv2.line(img,tuple(pointsList[round(size-1)]),(x,y),(0,0,255),2)
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointsList.append([x,y])
 
def gradient(pt1,pt2):
    try:
        return (pt2[1]-pt1[1]) / (pt2[0]-pt1[0]+1e-10)

    except ZeroDivisionError:
        return 0
 
def getAngle(pointsList):
    pt1, pt2 = pointsList[-2:]

    pt3 = [pt2[0],pt2[1]-100]
    cv2.line(img,tuple(pt2),pt3,(0,0,255),2)
    cv2.circle(img,pt3,5,(0,0,255),cv2.FILLED)

    m1 = gradient(pt2,pt1)
    print(m1)
    m2 = gradient(pt3,pt2)
    print(m2)
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = abs(round(math.degrees(angR), 3))
    cv2.putText(img,str(angD),(pt2[0]-40,pt2[1]-20),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2) 

while True:
    if len(pointsList) % 2 == 0 and len(pointsList) !=0:
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