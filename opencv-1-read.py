import  cv2

img = cv2.imread('Resources/lena.png')

cv2.imshow('lena',img)

cv2.waitKey(1000)
