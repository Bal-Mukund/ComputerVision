import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread(r'photos\narayan.JPG')
# cv.imshow("image", img)

# resizing if the image is too big for the monitor
dimension = (int(img.shape[0] * 0.18), int(img.shape[1] * 0.2))
image = cv.resize(img, dimension, interpolation=cv.INTER_AREA)
cv.imshow('Image', image)

# spliting color channels
blue, green, red = cv.split(image)
cv.imshow("blue", blue)

blank = np.zeros(image.shape[:2], dtype='uint8')

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# mask .....
circle = cv.circle(blank.copy(), (450,300), 100, 255, -1)
mask = cv.bitwise_and(gray,gray, mask=circle)
cv.imshow("mask", mask)

# calculating Histogram of grayscale Image
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('histogram representation')
# plt.xlabel('Pixel intensity')
# plt.ylabel('no. of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# histogram for all three channels blue, green, red
# color index =>  0 for blue, 1 for green, 2 for red ... B,G,R
colors = ('b', 'g', 'r')

plt.figure()
plt.title("color histogram")
plt.xlabel('colors pixel intensity')
plt.ylabel('no. of pixels')
for i, col in enumerate(colors):
    # circle for mask 
    hist = cv.calcHist([image], [i], None, [256], [0,256])
    plt.plot(hist)

plt.show()

# histogram for individual color
# histogram = cv.calcHist([img], [0], None, [256], [0, 256])

# plt.figure()
# plt.title("color histogram")
# plt.xlabel('colors pixel intensity')
# plt.ylabel('no. of pixels')
# plt.plot(histogram)
# plt.show()

cv.waitKey(0)