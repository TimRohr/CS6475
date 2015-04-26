# Final Project
# Timothy Rohr and David Whiskochil
# GTID's: 903137387 and 901293148

import cv2
import numpy as np
import scipy as sp
from PIL import Image
import requests
from StringIO import StringIO

PIL_Version = Image.VERSION

print PIL_Version

urlL = raw_input("Enter Left Image url")
responseL = requests.get(urlL)
imL = Image.open(StringIO(responseL.content))

urlR = raw_input("Enter Right Image url")
responseR = requests.get(urlR)
imR = Image.open(StringIO(responseR.content))

#imL = Image.open("left.JPG")
#imR = Image.open("right.JPG")


#imL.show()
print "IML Size=", imL.size

#imR.show()
print "IMR Size=", imR.size

if imL.size < imR.size:
    print "IML is smaller"
    imR=imR.resize(imL.size)
    print "resizing"
    
elif imL.size > imR.size:
    print "IMR is smaller"
    imL=imL.resize(imR.size)
    print "resizing"
    
else:
    print "they are equal."

print "IML Size=", imL.size
print "IMR Size=", imR.size

lsplit_red = np.array(imL)
lsplit_red[:,:,1]*=0
lsplit_red[:,:,2]*=0
temp_lsplit_red = Image.fromarray(lsplit_red)

rsplit_blue = np.array(imR)
rsplit_blue[:,:,0]*=0
rsplit_blue[:,:,1]*=0
temp_rsplit_blue = Image.fromarray(rsplit_blue)

#rsplit_cyan = np.array(imR)
#rsplit_cyan[:,:,2]*=0
#temp_rsplit_cyan = Image.fromarray(rsplit_cyan)

#####temp_lsplit_red.show()
#####temp_rsplit_blue.show()
#temp_rsplit_cyan.show()

total_image=lsplit_red+rsplit_blue

total_image = Image.fromarray(total_image)
######total_image.show()
#cv2.imwrite("total_image.jpg", total_image)
total_image.save("total_image.png","PNG")
           
