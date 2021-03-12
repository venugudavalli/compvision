import cv2 as cv
import numpy as np

img = cv.imread('photos/lady.jpg')
#print(img.shape)

cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(),(img.shape[1]//2 +45 ,img.shape[0]// 2),100,255, -1)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370),255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Sape',weird_shape )

#mask = cv.circle(blank, (img.shape[1]//2  + 45, img.shape[0]//2),100, 255, -1)
#mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2),(img.shape[1]//2  + 100, img.shape[0]//2 + 100),255, -1)
#cv.imshow('Mask circle', mask)

#masked = cv.bitwise_and(img, img, mask=mask)
#cv.imshow = cv.imshow('Masked Image', masked)
masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow = cv.imshow('Weird shaped Masked Image', masked)
cv.waitKey(0)