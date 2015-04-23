import cv2
#import PIL
import numpy as np
import scipy as sp

'''
#from image_split import showRed
imageLeft=cv2.imread("left.jpg",0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', imageLeft)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
"""#imageRight=cv2.imread("right.JPG")
print "test"
showRed(imageLeft)


#cv2.imwrite('red.jpg',showRed(imageleft))
"""


from PIL import Image

PIL_Version = Image.VERSION

print PIL_Version

#img_filename = "left.JPG"
#print "image Filename =", img_filename

imL = Image.open("rot_left.JPG")
#imL.show()
imR = Image.open("rot_right.JPG")
#imR.show()


'''
lsplit_blue = np.array(imL)
lsplit_blue[:,:,0]*=0
lsplit_blue[:,:,1]*=0
lsplit_blue = Image.fromarray(lsplit_blue)
lsplit_blue.show()

lsplit_red = np.array(imL)
lsplit_red[:,:,1]*=0
lsplit_red[:,:,2]*=0
lsplit_red = Image.fromarray(lsplit_red)
lsplit_red.show()

lsplit_green = np.array(imL)
lsplit_green[:,:,0]*=0
lsplit_green[:,:,2]*=0
lsplit_green = Image.fromarray(lsplit_green)
lsplit_green.show()

lsplit_cyan = np.array(imL)
lsplit_cyan[:,:,2]*=0
lsplit_cyan = Image.fromarray(lsplit_cyan)
lsplit_cyan.show()

rsplit_blue = np.array(imL)
rsplit_blue[:,:,0]*=0
rsplit_blue[:,:,1]*=0
rsplit_blue = Image.fromarray(rsplit_blue)
rsplit_blue.show()

rsplit_red = np.array(imL)
rsplit_red[:,:,1]*=0
rsplit_red[:,:,2]*=0
rsplit_red = Image.fromarray(rsplit_red)
rsplit_red.show()

rsplit_green = np.array(imL)
rsplit_green[:,:,0]*=0
rsplit_green[:,:,2]*=0
rsplit_green = Image.fromarray(rsplit_green)
rsplit_green.show()

rsplit_cyan = np.array(imL)
rsplit_cyan[:,:,2]*=0
rsplit_cyan = Image.fromarray(rsplit_cyan)
rsplit_cyan.show()
'''
rsplit_red = np.array(imR)
lsplit_cyan = np.array(imL)
lsplit_cyan[:,:,2]*=0
image_join=np.array(imR)
image_join=lsplit_cyan
image_join[:,:,2]=rsplit_red[:,:,2]
image_join = Image.fromarray(image_join)
image_join.show()
           
