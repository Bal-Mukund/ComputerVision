import cv2 as cv
import numpy as np

# contours are the boundaries of an image they are different from an edge of an image
img = cv.imread(r'photos\CHENNAI .jpg')
cv.imshow("Image", img)

blackCanvas = np.zeros(img.shape, dtype='uint8')

grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray image", grayImg)

blured = cv.GaussianBlur(grayImg, (7,7), cv.BORDER_DEFAULT)

canny = cv.Canny(blured, 125, 175)
cv.imshow("canny", canny)

# threshold ...... binarizing the image if the value is less than x then make it black if greater than x then make it white
ret, threshold = cv.threshold(blured, 125, 255, cv.THRESH_BINARY)
cv.imshow("threshold", threshold)

# finding contours
contours, hirearchy = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours(blackCanvas, contours, -1, (0,0,255), 1)
cv.imshow("blackcanvas", blackCanvas)

cv.waitKey(0)