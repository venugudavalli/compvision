import cv2 as cv
### Reading Image
#img = cv.imread('photos/cat_large.jpg')

#cv.imshow('Cat', img)

#cv.waitKey(0)

### Reading Videos for Test

capture = cv.VideoCapture('Videos/dog.mp4')

while True:

    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFf==ord('d'):
        break

capture.release()
cv.destroyAllWindows()