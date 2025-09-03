import numpy as np
import cv2
#i resized it to be able to see the full image
img=cv2.resize(cv2.imread("test.jpg"),None,fx=0.7,fy=0.7)
#created two copies one for shape detector and another for colour detector
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#highlights the shape
_, shaper = cv2.threshold(grey_img, 240 , 255, cv2.THRESH_BINARY)

colours=["red","yellow","blue","green"]
#bound and mask for four colours
lowboundy=np.array([20,100,100],dtype=np.uint8)
upboundy=np.array([30,255,255],dtype=np.uint8)
yellow_mask = cv2.inRange(hsv_img, lowboundy, upboundy)
red_lower1 = np.array([0, 120, 70], np.uint8) 
red_upper1 = np.array([10, 255, 255], np.uint8) 
red_lower2 = np.array([170, 120, 70], np.uint8) 
red_upper2 = np.array([180, 255, 255], np.uint8)
red_mask1 = cv2.inRange(hsv_img, red_lower1, red_upper1)  
red_mask2 = cv2.inRange(hsv_img, red_lower2, red_upper2)  
#red has 2 masks because it present in 2 hue values
red_mask=red_mask1|red_mask2
green_lower = np.array([35, 100, 100], np.uint8) 
green_upper = np.array([85, 255, 255], np.uint8) 
green_mask = cv2.inRange(hsv_img, green_lower, green_upper) 
blue_lower = np.array([94, 80, 2], np.uint8) 
blue_upper = np.array([120, 255, 255], np.uint8) 
blue_mask = cv2.inRange(hsv_img, blue_lower, blue_upper) 


def detector(colour,mask):
#i learned about contours and decieded to use the because they allow me to process multiple shapes in the same image each indivually
    shapes,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for shape in shapes:
        area =cv2.contourArea(shape)
        if area <350:
            continue
        x,y,w,h=cv2.boundingRect(shape)
        cv2.putText(img,colour,(x,y),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,0),1)

for colour in colours:
    if colour=="red":
        detector(colour,red_mask)


    elif colour=="green":
        detector(colour,green_mask)
        



    elif colour=="blue":
        detector(colour,blue_mask)



    elif colour=="yellow":
        detector(colour,yellow_mask)


#the frame is treated as a contour so i needed to set reter to tree instead of external
contours , hierarchy = cv2.findContours(shaper, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



for contour in contours:
    area=cv2.contourArea(contour)
    #the area checker is for filtering little dots that may count as a shape
    if area <200:
        continue
    #approximates the contour to a polygon
    approx = cv2.approxPolyDP(contour, 0.02* cv2.arcLength(contour, True), True)
    #gets the cordinates
    x, y , w, h = cv2.boundingRect(approx)
    #the main critirea here is the number of sides and the ratio between them
    if len(approx) == 3:
        cv2.putText( img, "Triangle", (x, y+30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )
    elif len(approx) == 4 :
       
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(img, "square", (x, y+30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        else:
            cv2.putText(img, "rectangle", (x, y+30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    
    else:
        cv2.putText(img, "circle", (x, y+30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv2.imshow("test",img)
cv2.waitKey(0)



