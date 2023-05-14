import cv2 as cv
import numpy as np

dog_image = cv.imread(r'photos\German-Shepherd-puppies.jpg')
cv.imshow("Dog", dog_image)

# grayscale an image ..........
grayscaled = cv.cvtColor(dog_image, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscaled Image', grayscaled)

# Gausian Blur ...........
blured = cv.GaussianBlur(dog_image, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blured" , blured)

#canny edge detection .........
edges = cv.Canny(blured, 125, 175)
cv.imshow("Edges", edges)

# dilating image .... meaning adding pixel to the bourdary of an image
dilated = cv.dilate(edges, (5,5), iterations=3)
cv.imshow("dilated", dilated)

# eroding an image ..... meaning removing pixel from boundry of an image .... opposite of dilating an image
eroded = cv.erode(dilated, (5,5), iterations=3)
cv.imshow("eroded", eroded)

cv.waitKey(0)