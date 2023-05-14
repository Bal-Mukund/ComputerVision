import cv2 as cv
import numpy as np

img = cv.imread(r'photos\German-Shepherd-puppies.jpg')
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

''' thresholding => if pixel value is less than threshold value
 then it will be black if greater then set it to 255 (white) '''
# simple thresholding
thresholdingValue, thresholdImage = cv.threshold(gray , 155, 255, cv.THRESH_BINARY)
cv.imshow("threshold image", thresholdImage)

# inverse threshold => act as the inverse of threshold
thresholdValue, inverseThresholdImage = cv.threshold(gray, 155, 255, cv.THRESH_BINARY_INV)
cv.imshow("inverse threshold Image", inverseThresholdImage)

# adaptive Thresholding => instead of manually giving threshold let the opencv decide the threshold value
adaptiveThresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow("adaptive Threshold", adaptiveThresh)


cv.waitKey(0)
