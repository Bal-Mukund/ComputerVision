import cv2 as cv
import numpy as np

blackCanvas = np.zeros((500, 500,3), dtype= 'uint8')
# cv.imshow('black', blackCanvas)

red = blackCanvas[:]
red[100:400, 100:400] = 0,0,255
# cv.imshow('red',red)

# drawing ...........
cv.rectangle(blackCanvas, (0,0), (255,255), (255,0,0), 2)
# cv.imshow("rectangle",blackCanvas)

cv.circle(blackCanvas, (255,255), 50, (0,255,0), 3)
# cv.imshow("Cirle", blackCanvas)

cv.line(blackCanvas, (0,0), (500,500), (255,255,255), 1)
# cv.imshow("line", blackCanvas)

cv.putText(blackCanvas, "abstract paintings" , (50,250), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0))
cv.imshow("Text", blackCanvas)

cv.waitKey(0)