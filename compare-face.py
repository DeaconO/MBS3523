import cv2
import numpy as np
import face_recognition
print(cv2.__version__)
print(face_recognition.__version__)

#Known_face
img_BG = face_recognition.load_image_file('image-known/Bill Gates.jpg')
img_BG = cv2.cvtColor(img_BG,cv2.COLOR_RGB2BGR)
BG_Loc = face_recognition.face_locations(img_BG)[0]
BG_encode = face_recognition.face_encodings(img_BG)[0]
print(BG_encode)

#Unknown_face
img_unknown = face_recognition.load_image_file('image-Unknown/test_image_2.jpg')
img_unknown = cv2.cvtColor(img_unknown,cv2.COLOR_RGB2BGR)
#unknown_Loc = face_recognition.face_locations(img_unknown)[0]
#unknown_encode = face_recognition.face_encodings(img_unknown)[0]

#compare_face
#results = face_recognition.compare_faces([BG_encode],unknown_encode,0.5)
#print(results)
#dist = face_recognition.face_distance([BG_encode],unknown_encode)
#print(dist)

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    face_Loc = face_recognition.face_locations(imgRGB)[0]
    face_encode = face_recognition.face_encodings(imgRGB)[0]
    # compare_face
    results = face_recognition.compare_faces([BG_encode], face_encode, 0.5)
    print(results)
    dist = face_recognition.face_distance([BG_encode], face_encode)
    print(dist)

    cv2.rectangle(img_BG,(BG_Loc[3],BG_Loc[0]),(BG_Loc[1],BG_Loc[2]),(0,255,0),2)
    cv2.rectangle(img,(face_Loc[3],face_Loc[0]),(face_Loc[1],face_Loc[2]),(0,255,0),2)

    cv2.imshow('Photo BG' , img_BG)
    cv2.imshow('Photo_UN',img)

    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.waitKey(0)
