import cv2, time
video = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    check, frame = video.read()

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.15, minNeighbors = 5)
    
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), color=(0, 255, 0), thickness=3)

    out.write(frame)
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(10)

    if key == ord("q"):
        break

video.release()
out.release()
cv2.destroyAllWindows()
