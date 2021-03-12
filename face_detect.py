import cv2 as cv

#img = cv.imread('Photos/lady.jpg')
#cv.imshow('Person', img)
img = cv.imread('Photos/travel.jpg') 
cv.imshow('Group of 5 People', img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray Person', gray)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

print(f'Number of Faces found = {len(faces_rect)}')

for (x, y, w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),thickness=2)

cv.imshow('Dectected Faces', img)
cv.waitKey(0)