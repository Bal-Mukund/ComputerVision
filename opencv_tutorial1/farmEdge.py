import cv2 as cv
import numpy as np

img = cv.imread(r'photos\farm 2.jpg')
height, width = img.shape[:2]

dimension = (int(img.shape[1] * 0.80), int(img.shape[0] * 0.90))
resize = cv.resize(img, dimension, interpolation=cv.INTER_AREA)

gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,  (9,9), 0)

canny = cv.Canny(blur, 155, 175)

cv.imshow("gray", gray)
cv.imshow("resized", resize)
cv.imshow("edges", canny)
cv.imshow("blur", blur)

cv.waitKey(0) 
