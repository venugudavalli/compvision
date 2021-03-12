import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# Simple thresholding
threshold, thresh = cv.threshold(gray,225, 255,cv.THRESH_BINARY)
#print('Threshold', threshold)
cv.imshow('Simple Threshold', thresh)

# threshold, thresh_inv = cv.threshold(gray,150, 255,cv.THRESH_BINARY_INV)
# print('Threshold', threshold)
# cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
#adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
#adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,9) # Inverse
#adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow('Adaptive Threshold', adaptive_thresh)


cv.waitKey(0)
