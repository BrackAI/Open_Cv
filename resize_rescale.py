import cv2 as cv
scale=0.75
#img =cv.imread('Photos/cat_large.jpg')
#cv.imshow('Cat',img)

def rescaleFrame(frame):

    width=int(frame.shape[1] * scale)#width of my frame or image

    height=int(frame.shape[0] * scale)# it's basically height of my image or frame

    dimensions = (width,height)

    return cv.resize(frame , dimensions, interpolation=cv.INTER_AREA)

capture=cv.VideoCapture('Videos/Nature1.mp4')

while True:
    isTrue, frame=capture.read()#read video frame by frame

    frame_resized=rescaleFrame(frame)

    cv.imshow('Video',frame)

    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) &0xFF==ord('d'):#here d means when d is presed than the video is stoped
        break

capture.release()

cv.destroyAllWindows()