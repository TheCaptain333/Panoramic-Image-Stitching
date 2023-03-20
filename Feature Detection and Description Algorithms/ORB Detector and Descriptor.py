import numpy as np
import cv2

filename = 'map1.jpg'
img=cv2.imread(filename,cv2.IMREAD_GRAYSCALE)



orb = cv2.ORB_create()

kp = orb.detect(img,None)

_,des = orb.compute(img,kp)

img_new = cv2.drawKeypoints(img,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

print(len(kp))
cv2.imshow("ORB Detector",img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()


















