import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('Photos/park.jpg')
cv.imshow('Image', img)

#plt.imshow(img)
#plt.show()





#BGR to Grayscale
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gary',gray)

#BGR TO HSV
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR TO LAB
lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab',lab)

#BGR to RGB
rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()




cv.waitKey(0)