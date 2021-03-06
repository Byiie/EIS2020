import cv2
import numpy as np
cap = cv2.VideoCapture(0)
lower_blue=np.array([100,43,46])
upper_blue=np.array([124,255,255])
def camera():
    while True:
        ret, img= cap.read()
        ymax,xmax,leni = img.shape
        imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        blueobj=cv2.inRange(imghsv,lower_blue,upper_blue)
        conts,hrc=cv2.findContours(blueobj,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        img = cv2.drawContours(img, conts, -1, (0,0,255), 3)
        bigconts=[]
        for cont in conts:
            area = cv2.contourArea(cont)
            if area >200:
                bigconts.append(cont)
                img = cv2.drawContours(img, bigconts, -1, (255,0,0), 10)
                for bigycnt in bigconts:
                    M=cv2.moments(bigycnt)
                    cx=int(M['m10']/M['m00'])
                    cy=int(M['m01']/M['m00'])
                    cv2.circle(img,(cx,cy),50,(0,0,255),5)
                    break
                cv2.imshow("blueobj",blueobj)
                cv2.imshow("window",img)
                key = cv2.waitKey(1) & 0xFF

