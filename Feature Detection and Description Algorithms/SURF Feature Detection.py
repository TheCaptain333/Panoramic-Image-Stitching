import numpy as np
import cv2

filename = 'map1.jpg'
img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

surf = cv2.xfeatures2d.SURF_create(400)

kp,des = surf.detectAndCompute(img,None)

img_new = img
img_new = cv2.drawKeypoints(img,kp,img_new)

cv2.imshow("SURF Feature Detection",img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()


























