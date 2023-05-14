import cv2 as cv
import numpy as np

img = cv.imread(r'photos\rolls-royce-phantom.jpg')
cv.imshow("image", img)

# willl show all the channels in grayscale brighter the area means more that color is present in that area and vice versa
b, g, r = cv.split(img)

# cv.imshow("blue", b)  
# cv.imshow("green", g)
# cv.imshow("red", r)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("blank",blank)


#showing individual channels by merging them with black 
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

merge = cv.merge([b, g, r])
cv.imshow("merge", merge)


cv.waitKey(0)