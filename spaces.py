import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

#plt.imshow(img)
#plt.show()
# BGR to Grayscale

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Park', gray)

# # BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV Park', hsv)

# # BGR to L+A+B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab Park', lab)

# BGR -> RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB Park', rgb)
#plt.imshow(rgb)
#plt.show()

# HSV -> BGR
hsv_bgr  = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr Park', hsv_bgr)

# L+A+B -> BGR
lab_bgr  = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab_bgr Park', lab_bgr)
cv.waitKey(0)
