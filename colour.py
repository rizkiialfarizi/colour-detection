import cv2
import numpy as np
from PIL import Image, ImageTk

#capturing video through webcam
cap=cv2.VideoCapture(0)

while(1):
        _, img = cap.read()

        #converting frame(img i.e BGR) to HSV (hue-saturation-value)

        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        #defining the range of red color
        red_lower=np.array([136,87,111],np.uint8)
        red_upper=np.array([180,255,255],np.uint8)

        #defining the range of blue color
        blue_lower=np.array([99,115,150],np.uint8)
        blue_upper=np.array([110,255,255],np.uint8)

        #defining the range of green color
        green_lower=np.array([50,100,100],np.uint8)
        green_upper=np.array([70,255,255],np.uint8)

        #defining the range of yellow color
        yellow_lower=np.array([20,100,100],np.uint8)
        yellow_upper=np.array([40,2555,255],np.uint8)
        
        #defining the range of purple color
        purple_lower=np.array([120,100,100],np.uint8)
        purple_upper=np.array([140,255,255],np.uint8)

        #defining the range of brown color
        brown_lower=np.array([98,100,100],np.uint8)
        brown_upper=np.array([118,255,255],np.uint8)

        #finding the range of red,blue and yellow color in the image
        red=cv2.inRange(hsv, red_lower, red_upper)
        blue=cv2.inRange(hsv, blue_lower, blue_upper)
        green=cv2.inRange(hsv, green_lower, green_upper)
        yellow=cv2.inRange(hsv, yellow_lower, yellow_upper)
        purple=cv2.inRange(hsv,purple_lower,purple_upper)
        brown=cv2.inRange(hsv,brown_lower,brown_upper)

        #Morphologic transformation, Dilatation
        kernal = np.ones((5 ,5), "uint8")

        red=cv2.dilate(red, kernal)
        res=cv2.bitwise_and(img, img, mask = red)

        blue=cv2.dilate(blue, kernal)
        res1=cv2.bitwise_and(img, img, mask = blue)

        green=cv2.dilate(green, kernal)
        res2=cv2.bitwise_and(img, img, mask = green)

        yeloow=cv2.dilate(yellow, kernal)
        res3=cv2.bitwise_and(img, img, mask = yellow)

        purple=cv2.dilate(purple,kernal)
        res4=cv2.bitwise_and(img, img, mask = purple)

        brown=cv2.dilate(brown,kernal)
        res5=cv2.bitwise_and(img, img, mask = brown)

        #Trackig the Red Color
        contours,hierachy=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>300):

                        x,y,w,h = cv2.boundingRect(contour)
                        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                        cv2.putText(img,"Merah",(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))

        #Trackig the Blue Color
        contours,hierarchy=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>300):

                        x,y,w,h = cv2.boundingRect(contour)
                        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                        cv2.putText(img,"Biru",(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))

        #Trackig the Green Color
        contours,hierarchy=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>300):

                        x,y,w,h = cv2.boundingRect(contour)
                        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                        cv2.putText(img,"Hijau",(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))

        #Trackig the yellow Color
        contours,hierarchy=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>300):

                        x,y,w,h = cv2.boundingRect(contour)
                        img = cv2.rectangle(img,(x,y),(x+w,y+h),(40,255,255),2)
                        cv2.putText(img,"kuning",(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))

        #Trackig the purple Color
        contours,hierarchy=cv2.findContours(purple,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>300):

                        x,y,w,h = cv2.boundingRect(contour)
                        img = cv2.rectangle(img,(x,y),(x+w,y+h),(119,63,158),2)
                        cv2.putText(img,"ungu",(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))

        #Trackig the purple Color
        contours,hierarchy=cv2.findContours(brown,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area>300):

                        x,y,w,h = cv2.boundingRect(contour)
                        img = cv2.rectangle(img,(x,y),(x+w,y+h),(118,255,255),2)
                        cv2.putText(img,"coklat",(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))

                        
         #cv2.imshow("Redcolor",red)
        cv2.imshow("Pembaca Warna",img)
        #cv2.imshow("merah",res)
        if cv2.waitKey(10) & 0xFF == ord('`'):
                cap.release()
                cv2.destroyAllWindows()
                break
