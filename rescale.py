import cv2 as cv
### Reading Image
img = cv.imread('photos/cat.jpg')

cv.imshow('Cat', img)

def changeRes(width, height):
    # Live Video only from We bcams or external cameras
    capture.set(3, width)
    capture.set(4, height)

def rescaleFrame(frame, scale=0.75):
    # Works for Images, Videos and Live Video
    #if frame is not None:
    width = int(frame.shape[1] * scale)
    height =  int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Resized Image', resized_image)
cv.waitKey(0)
### Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:

    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,0.25)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFf==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

