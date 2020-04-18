import cv2
import numpy as np

green = np.uint8([[[210,105,30]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
lowerLimit = hsv_green[0][0][0] - 10, 100, 100
upperLimit = hsv_green[0][0][0] + 10, 255, 255
print (hsv_green)
print (lowerLimit)
print (upperLimit)

