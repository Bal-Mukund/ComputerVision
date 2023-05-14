import cv2 as cv
import numpy as np

img = cv.imread(r'photos\newYork.jpg')
dimension = (int(img.shape[0] * 0.2), int(img.shape[1] * 0.1))
resized = cv.resize(img, dimension, interpolation=cv.INTER_AREA)
cv.imshow("resized", resized)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# laolacian edge detection
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("laplacian", lap)

# sobel edge detection
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobelCombined = cv.bitwise_or(sobelx, sobely)

# cv.imshow("sobelx", sobelx)
# cv.imshow("sobely", sobely)
cv.imshow("sobel combined", sobelCombined)

# canny edge detection 
canny = cv.Canny(gray, 155, 175)
cv.imshow("canny", canny)

cv.waitKey(0)