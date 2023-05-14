import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r'photos\CHENNAI .jpg')
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("gray",gray)

# bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

# bgr to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# plt.imshow(img)
# plt.show()

# gray to bgr -> no you can't convert an grayscale image back to bgr or rgb

# hsv to bgr
hsv2bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv2bgr", hsv2bgr)

# lab to bgr
lab2bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("lab2bgr", lab2bgr)

cv.waitKey(0)
