'''
import numpy as np 
import cv2 as cv 
def get_limits(color):
    c=np.uint8([[color]])#here insert the bgr value which you want to convert to hsv
    hsvC=cv.cvtColor(c,cv.COLOR_BGR2HSV)

    lowerlimit=hsvC[0][0][0]-10,100,100
    upperlimit=hsvC[0][0][0]+10,100,100

    lowerlimit=np.array(lowerlimit,dtype=np.uint8)
    upperlimit=np.array(upperlimit,dtype=np.uint8)

    return lowerlimit, upperlimit'''

import numpy as np
import cv2 as cv


def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit