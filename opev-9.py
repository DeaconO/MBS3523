import cv2

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('Resources/guitar.mp4')


while True:
    success , img = cap.read()
    faces = faceCascade.detectMultiScale(img, 1.05, 5)
    print(faces)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('kitten',img)
        if cv2.waitKey(20) & 0xff == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()