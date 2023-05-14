import numpy as np
import cv2 as cv

# # matrix = np.float32([[1,0,100], [0,1,100]])
# # print(matrix)

# # img = cv.imread(r'photos\without1.JPG')
# # dimension = (img.shape[0], img.shape[1])
# # print(dimension)

# img = cv.imread(r'photos\German-Shepherd-puppies.jpg')
# # cv.imshow("image", img)
# dimension = (img.shape[0], img.shape[1])
# print(dimension)
# cv.imshow("puppy", img)
# print("##############")

# image = cv.imread(r'photos\without1.JPG')
# print(image.shape[:2])
# dimension = (int(image.shape[0] * 0.21), int(image.shape[1] * 0.15))
# print(dimension)
# resize = cv.resize(image, dimension, interpolation=cv.INTER_AREA)
# cv.imshow("Iphone Resized", resize)
# print("############")

# image = cv.imread(r'photos\with1.JPG')
# print(image.shape[:2])
# dimension = (int(image.shape[0] * 0.17), int(image.shape[1] * 0.19))
# print(dimension)
# resize = cv.resize(image, dimension, interpolation=cv.INTER_AREA)
# cv.imshow("Iphone Resized2", resize)

# cv.waitKey(0)

img = cv.imread(r'photos\CHENNAI .jpg')

cv.imshow("image", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

dimension = img.shape[:]
print(dimension)

dimension2 = gray.shape[:]
print(dimension2)

cv.waitKey(0)