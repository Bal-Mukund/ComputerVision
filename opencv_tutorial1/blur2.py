import cv2 as cv
import numpy as np

img = cv.imread(r'photos\CHENNAI .jpg')
cv.imshow("image", img)

print(img)

blur = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("blur", blur)

cv.waitKey(0)