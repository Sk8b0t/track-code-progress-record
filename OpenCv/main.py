# import cv2 as cv
# img=cv.imread('neymar.jpg')
# cv.imshow('neymar',img)
# capture=cv.VideoCapture('aot.mp4')
# while True:
#     bool,frame=capture.read()
#     cv.imshow("ATTACK ON TITAN",frame)
#     # basically if the letter 'd' is pressed then the video stops playing 
#     if cv.waitKey(11) & 0xFF==ord('d'):  #bitwise operation
#         break
# capture.release()
# cv.destroyAllWindows()

import cv2 as cv

def showImage(img):
    img2=cv.imread(img)
    cv.imshow("Image",img2)
    cv.waitKey(0)

def showVideo(vid):
    cap=cv.VideoCapture(vid)
    while True:
        bool,frame= cap.read()
        cv.imshow("video",frame)
        if cv.waitKey(11) & 0xFF==ord('d'):
            break
    cap.release()
    cv.destroyAllWindows()

if __name__=="__main__":
    showImage("neymar.jpg")
    showVideo("aot.mp4")



