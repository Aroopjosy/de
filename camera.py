import cv2 as cv

webcam = cv.VideoCapture(0)
face_detect = cv.CascadeClassifier('./data.xml')
while True:
  flag ,frame = webcam.read()
  frame = cv.flip(frame, 1,1)
  if flag:
      faces = face_detect.detectMultiScale(frame)
      for x,y,w,h in faces:
          cv.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

  cv.imshow("live", frame)
  if cv.waitKey(2) == 27:
    break
webcam.release()
cv.destroyAllWindows()