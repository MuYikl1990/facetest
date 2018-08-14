import requests
import cv2

face_patterns = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #分类器
image_sample = cv2.imread('D:/\//PyCharm/examples/github/facetest/face/media/image/pic.jpg')
faces = face_patterns.detectMultiScale(image_sample, scaleFactor=1.1, minNeighbors=5, minSize=(10,10))
num = 0
for (x,y,w,h) in faces:
	cv2.rectangle(image_sample, (x,y), (x+w, y+h), (0,255,0),2) #左下角，右上角，线颜色，线宽
	num += 1
#cv.imshow('face', image_sample) 
print(num)
cv2.imwrite('D:/\//PyCharm/examples/github/facetest/face/media/image/show.jpg', image_sample)
cv2.waitKey(0)
