import numpy as np
import cv2
img=cv2.GaussianBlur(cv2.resize(cv2.imread("test.jpg"),None,fx=0.7,fy=0.7),(3,3),cv2.BORDER_DEFAULT)
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
result=img
colours=["red","yellow","blue","green"]
lowboundy=np.array([20,100,100],dtype=np.uint8)
upboundy=np.array([30,255,255],dtype=np.uint8)
yellow_mask = cv2.inRange(hsv_img, lowboundy, upboundy)
red_lower = np.array([136, 87, 111], np.uint8) 
red_upper = np.array([180, 255, 255], np.uint8) 
red_mask = cv2.inRange(hsv_img, red_lower, red_upper)  
green_lower = np.array([35, 100, 100], np.uint8) 
green_upper = np.array([85, 255, 255], np.uint8) 
green_mask = cv2.inRange(hsv_img, green_lower, green_upper) 
blue_lower = np.array([94, 80, 2], np.uint8) 
blue_upper = np.array([120, 255, 255], np.uint8) 
blue_mask = cv2.inRange(hsv_img, blue_lower, blue_upper) 
r=cv2.GaussianBlur(red_mask,(5,5),cv2.BORDER_DEFAULT)

def detector(colour,mask):
    shapes,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for shape in shapes:
        area =cv2.contourArea(shape)
        if area <350:
            continue
        x,y,w,h=cv2.boundingRect(shape)
        cv2.putText(img,colour,(x,y),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,0),1)

for colour in colours:
    if colour=="red":
        detector(colour,r)


    elif colour=="green":
        detector(colour,green_mask)
        



    elif colour=="blue":
        detector(colour,blue_mask)



    elif colour=="yellow":
        detector(colour,yellow_mask)
cv2.imshow("test",img)
cv2.waitKey(0)


