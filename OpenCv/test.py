import cv2 as cv

def newDimention(frame, scale=0.75):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    d=(width,height)
    return cv.resize(frame,d,interpolation=cv.INTER_AREA)

img=cv.imread("neymar2.jpg")
cv.imshow("njr",img)
cv.imshow("njr",newDimention(img,(480,720)))
cv.waitKey(0)