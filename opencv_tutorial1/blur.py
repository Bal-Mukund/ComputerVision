import cv2 as cv
import numpy as np

img = cv.imread(r'photos\CHENNAI .jpg')
cv.imshow("image", img)

""" average bluring => blur by calculating the average
    of all the surrounding rows and columns for the centre most """
average = cv.blur(img, (3,3))
cv.imshow('average blur', average)

""" Gausina blur => similar as average blur but each cell
    is given different weight in calculation of average for the ceter most cell """
gausian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("gausian", gausian)

""" median Blur => intsead of calulating the average it calulate the median of all the surrounding cell
    for the center most cell """
median = cv.medianBlur(img, 3)
cv.imshow("median", median)

""" Biletral blur => one of most advanced blur is retain the edges while bluring an image"""
biletral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("biletral blur", biletral)

cv.waitKey(0)