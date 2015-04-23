import cv2
#from opencv import highgui
#from time import sleep

from final_video import createAna

imageLeft=cv2.imread("left.JPG")
imageRight=cv2.imread("right.JPG")

createAna(imageLeft, imageRight)
