import cv2
import numpy as np

ear_cascade1 = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml')
ear_cascade2 = cv2.CascadeClassifier('haarcascade_mcs_rightear.xml')

cap = cv2.VideoCapture(0)

while 1:
  ret, img = cap.read()


  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  left_ear = ear_cascade1.detectMultiScale(gray, 1.2, 5)
  right_ear = ear_cascade2.detectMultiScale(gray, 1.2, 5)


  for (x,y,w,h) in left_ear:
      cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)

  for (x,y,w,h) in right_ear:
      cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)

  cv2.imshow('img',img)
  k = cv2.waitKey(30) & 0xff
  if k == 27:
      break


cap.release()
cv2.destroyAllWindows()