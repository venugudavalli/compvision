import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Cat',img)

#Converting to Grey scale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blurr

#blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

# Edge Cascade
#canny = cv.Canny(img,125,175)
#cv.imshow('Canny Edges', canny)

#canny = cv.Canny(blur,125,175)
#cv.imshow('Canny Edges', canny)

# Dilating the image

#dialated = cv.dilate(canny, (7,7),iterations=3)
#cv.imshow('Dialated', dialated)

#eroded = cv.erode(dialated,(7,7),iterations=3)
#cv.imshow('Eroded', eroded)

# Resize

resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC) # cv.INTER_AREA or cv.INTER_LINEAR
cv.imshow('Resized', resized)

# Cropping

cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)

