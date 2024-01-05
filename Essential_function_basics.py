import cv2 as cv

img=cv.imread('Photos/park.jpg')
#cv.imshow('Cat',img)

#converting image to grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur image
blur=cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(blur , 125, 175)
cv.imshow('Edges', canny)

#Dilating the image

dilated= cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

#Eroding(used to back the previous step)
eroded= cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

#Resize
resized=cv.resize(img,(500,500))
cv.imshow('Resized',resized)

#Crroping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
