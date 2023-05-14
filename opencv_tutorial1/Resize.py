import cv2 as cv 

#reading images

# image = cv.imread('photos\German-Shepherd-puppies.jpg')
# cv.imshow("dog",image)
# cv.waitKey(0)

#displaying videos
capture = cv.VideoCapture(r'C:\Users\balmu\opencv_tutorial1\videos\dog_video.mp4')

# for resizing an existing video or an image
def resize(frame, size= 0.5):
    height = int(frame.shape[0] * 0.8)
    width = int (frame.shape[1] * 0.2)
    dimension = (height, width)

    return cv.resize(frame, dimension)

while True:
    isTrue, frame = capture.read()
    resized = resize(frame)
    cv.imshow('resized', resized)
    if cv.waitKey(1) == ord(' '):
        break


capture.release()
cv.destroyAllWindows() 