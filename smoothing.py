import cv2 as cv
#import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging

average = cv.blur(img, (3,3))
cv.imshow('Avergae Blur', average)

# Gaussian Blurr

gauss = cv.GaussianBlur(img, (7,7),0)
cv.imshow('Gaussian Blur', gauss)

# Median Blurr
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blurr
bilateral = cv.bilateralFilter(img,10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)