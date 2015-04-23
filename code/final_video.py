import cv2
#from opencv import highgui
#from time import sleep

def makeMagic(left, right, out):
      chans=[]
      for i in range(6):
          chans.append(cv2.CreateImage(cv2.GetSize(left),8,1))
          cv2.Split(left, chans[0], chans[1], chans[2], None)
          cv2.Split(right, chans[3], chans[4], chans[5], None)
          cv2.Merge(chans[3],chans[4],chans[2], None, out)

  #cv.cvMerge(None,chans[1],None, None, out);

#cam=[]
def createAna(imageLeft, imageRight):
#  cam.append(highgui.cvCreateCameraCapture(0))
#  cam.append(highgui.cvCreateCameraCapture(1))
    cv2.namedWindow ("carrots", cv2.CV_WINDOW_AUTOSIZE)
#    imageLeft=cv2.imread("left.JPG")
#    imageRight=cv2.imread("right.JPG")
#    uno=highgui.cvQueryFrame(cam[0]);
#    dos=highgui.cvQueryFrame(cam[1]);
    uno=imageLeft
    dos=imageRight
    #highgui.cvShowImage("carrots",uno)
    cv2.imwrite('LEFTUSED.jpg',uno)
    cv2.waitKey(0)
    #highgui.cvShowImage("carrots",dos)
    cv2.imwrite('RIGHTUSED.jpg',dos)
    cv2.waitKey(0)
    merge=cv2.createImage(cv2.GetSize(uno),8,3)
    makeMagic(uno, dos, merge)
    cv2.showImage("carrots",merge);
    cv2.waitKey(0)
#    while True :
#        uno=highgui.cvQueryFrame(cam[0]);
#        dos=highgui.cvQueryFrame(cam[1]);
#        makeMagic(uno, dos, merge);
#        highgui.cvShowImage("carrots",merge);
#    if highgui.cvWaitKey(1)=="s":
#        cam.append(cam.pop(0))
#    print "tick"

#if __name__=="__main__":
#main()
