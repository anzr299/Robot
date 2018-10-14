import cv2
import sys
import serial
import io
import pyttsx


engine = pyttsx.init()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
img = cv2.imread('emoji.jpeg',1)
img1 = cv2.imread('emoji1.png',1)
ser = serial.Serial("/dev/ttyACM0" ,9600)
while True:
    cv2.imshow('emoji', img1)
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    if len(faces) > 0:
                face_no = 0
		print "face found!"
		ser.write('y'.encode()) 

    elifif len(faces) == 0:
                face_no +=1
                if face_no > 2:
		
		cv2.imshow('emoji', img
					


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
