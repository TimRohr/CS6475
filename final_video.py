import cv2
#from opencv import highgui
#from time import sleep

def makeMagic(left, right, out):
      chans=[]
      for i in range(6):
          chans.append(cv.cvCreateImage(cv.cvGetSize(left),8,1))
          cv.cvSplit(left, chans[0], chans[1], chans[2], None);
          cv.cvSplit(right, chans[3], chans[4], chans[5], None);
          cv.cvMerge(chans[3],chans[4],chans[2], None, out);

  #cv.cvMerge(None,chans[1],None, None, out);

#cam=[]
def main():
#  cam.append(highgui.cvCreateCameraCapture(0))
#  cam.append(highgui.cvCreateCameraCapture(1))
    highgui.cvNamedWindow ("carrots", highgui.CV_WINDOW_AUTOSIZE)
    imageLeft=cv2.imread("left.JPG")
    imageRight=cv2.imread("right.JPG")
#    uno=highgui.cvQueryFrame(cam[0]);
#    dos=highgui.cvQueryFrame(cam[1]);
    uno=imageLeft
    dos=imageRight
    highgui.cvShowImage("carrots",uno);
    highgui.cvWaitKey(0);
    highgui.cvShowImage("carrots",dos);
    highgui.cvWaitKey(0);
    merge=cv.cvCreateImage(cv.cvGetSize(uno),8,3)
    makeMagic(uno, dos, merge)
    highgui.cvShowImage("carrots",merge);
    highgui.cvWaitKey(0);
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
