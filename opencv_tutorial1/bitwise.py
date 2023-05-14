import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
cv.imshow("blank", blank)

# .copy() => drawing will be on a copy of blank not on the same blank
circle = cv.circle(blank.copy(), (blank.shape[0] // 2, blank.shape[1] // 2), 170, 255, -1)
cv.imshow("circle", circle)

rectangle = cv.rectangle(blank.copy(), (50,50), (350,350), 255, -1)
cv.imshow("rectangle", rectangle)

# bitwise And => intersection only
bitwiseAnd = cv.bitwise_and(circle, rectangle)
cv.imshow("bitwise and", bitwiseAnd)

# bitwise or  => intersection and non intersection both
bitwiseOr = cv.bitwise_or(circle,rectangle)
cv.imshow("bitwiseOr", bitwiseOr)

# bitwise xor  => non intersection only
bitwiseXor = cv.bitwise_xor(circle, rectangle)
cv.imshow("bitwise xor", bitwiseXor)

# bitwise not  => return inverse,   the compliment 
bitwiseNot = cv.bitwise_not(rectangle)
cv.imshow("bitwise Not", bitwiseNot)

cv.waitKey(0)