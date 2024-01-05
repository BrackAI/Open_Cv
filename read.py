import cv2 as cv
img = cv.imread('Photos/cat_large.jpg')#takes path an image and returns that image as a matrix of pixels
cv.imshow('Cat',img)#show image in an window and it takes name of window and the pixles of matrix
cv.waitKey(0)#specific delay in millisecond