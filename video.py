import cv2 as cv

capture=cv.VideoCapture('Videos/Nature1.mp4')

while True:
    isTrue, frame=capture.read()#read video frame by frame
    cv.imshow('Video',frame)
    if cv.waitKey(20) &0xFF==ord('d'):#here d means when d is presed than the video is stoped
        break

capture.release()
cv.destroyAllWindows()

