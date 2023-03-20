import numpy as np
import cv2

filename = 'map1.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp = sift.detect(gray,None)

img_new = gray
img_new = cv2.drawKeypoints(gray,kp,img_new,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("SIFT Features Detection",img_new)
cv2.waitKey(0)

kp,des = sift.compute(gray,kp)



cv2.destroyAllWindows()
























