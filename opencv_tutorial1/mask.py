import cv2 as cv
import numpy as np

# masking => removing the di-selected area of an image

img = cv.imread(r'photos\German-Shepherd-puppies.jpg')
cv.imshow("image", img)

# masking picture dimesion should exactly match with the original picture
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("blank", blank)

circle = cv.circle(blank.copy(), (400,175), 100, 255, -1)
cv.imshow("circle", circle)
rectangle = cv.rectangle(blank.copy(), (300,100), (500,250), 255, -1)
cv.imshow("rectangle", rectangle)

weiredShape = cv.bitwise_and(circle, rectangle)
cv.imshow("weired Shape", weiredShape)

# masking .......
masked = cv.bitwise_and(img, img, mask=weiredShape)
cv.imshow("masked", masked)

cv.waitKey(0)
