import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3),dtype='uint8')#creating blank image(width,heigth,Number of color channel)

cv.imshow('Blank',blank)

"""#paint the image at certain color#
blank[:] = 255,0,255#paint the whole image
cv.imshow('Green',blank)
blank[150:300 , 200:400] = 255,0,255#paint the  image with a range
cv.imshow('Green',blank)"""
#putiing shape
cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=2)
cv.imshow('Rectangle',blank)

#write text on image
cv.putText(blank, 'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0),2)
cv.imshow('Text',blank)


cv.waitKey(0)