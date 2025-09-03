# results:

<img width="1875" height="980" alt="Screenshot 2025-09-03 040517" src="https://github.com/user-attachments/assets/80ae6db3-1abb-42b6-98b1-48ad1042104f" />

# first thoughts:

the first thing that came to my mind was using edge detection and regular masks but after some thought i realized it wont work due to the presence of multiple shapes in the image
and the need to label each one indivually

#problem faced:

-  red mask caused a bit of a problem which was solved by using 2 masks for it

-  detecting shapes with rete external caused a bit of a problem,solved by swiching to tree

-  the epsillon needed some adjustments in order to register some shapes correctly

#the code itself:

it creates masks for red,green,blue and yellow the applies them then analiyzes each shape and gives it a label according to the mask that was used
it also applies a gray colour to a copy of the image and thresholds it to identify shapes
it counts the sides of each shape to determine its type with calculating the ratio between its sides in case the number of sides equals 4



