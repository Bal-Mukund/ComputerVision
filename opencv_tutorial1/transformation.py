import cv2 as cv
import numpy as np

img = cv.imread(r'photos\German-Shepherd-puppies.jpg')
cv.imshow("image", img)

# translation ..... shifting an image
def translation(image, x, y):
    translationMatrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, translationMatrix, dimensions)

# -x  => left
#  x  => right
# -Y  => up
#  Y  => down 

translated = translation(img, 100, 100)
# cv.imshow("translation", translated)

# Rotation 
def rotate(image, angle):
    (height, width) = image.shape[:2]
    rotationPoint = (height / 2, width / 2)
    rotationMatrix = cv.getRotationMatrix2D(rotationPoint,angle, 1.0)
    dimension = (width, height)
    return cv.warpAffine(image, rotationMatrix, dimension)

rotated = rotate(img, -90)
# cv.imshow("rotated", rotated)

# fliping an image ...........
fliped = cv.flip(img, 1)
cv.imshow("fliped", fliped)

#  0  =>  flip vertically
#  1  =>  flip horizontally
# -1  =>  flip both vertically and horizontally

cv.waitKey(0)