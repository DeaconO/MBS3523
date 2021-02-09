import  cv2
print(cv2.__version__)


cap = cv2.VideoCapture(0)

while True:
    success , img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('hm',img)
    # cv2.imshow('hm', imgGray)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()