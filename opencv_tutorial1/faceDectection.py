import cv2 as cv
import numpy as np

# loading harcascade classifier model
model = cv.CascadeClassifier(r'faceHardcascade.xml')

# img = cv.imread(r'photos\with1.JPG')

# dimension = (int(img.shape[0] * 0.17), int(img.shape[1] * 0.19))
# # print(dimension)
# resize = cv.resize(img, dimension, interpolation=cv.INTER_AREA)
# cv.imshow("image", resize)
# gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

# rectCordinate = model.detectMultiScale(gray, 1.1, 3)
# print(len(rectCordinate))

# for x,y,w,h in rectCordinate:
#     pt1 = (x,y)
#     pt2 = (x + w, y + h)

#     cv.rectangle(resize, pt1, pt2, (0,255,0), 2)
# cv.imshow("face", resize)
# cv.waitKey(0)

# face detection in videos ................

capture = cv.VideoCapture(0)

while True:
    _, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # rectCoordinate = model.detectMultiScale()
    rectCoordinate = model.detectMultiScale(gray, 1.1, 5)
    for x,y,w,h in rectCoordinate:
        pt1 = (x,y)
        pt2 = (x + w, y + h)
        cv.rectangle(frame, pt1, pt2, (0,255,0), 2)
        cv.imshow("live", frame)    

    if cv.waitKey(1) == ord(" "):
        break

print(len(rectCoordinate))
capture.release()
cv.destroyAllWindows()