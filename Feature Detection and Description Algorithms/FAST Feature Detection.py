import numpy as np
import cv2
import matplotlib.pyplot as plt


filename = "map1.jpg"
img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

fast = cv2.FastFeatureDetector_create(70)

kp=fast.detect(img,None)

img_new = img
img_new = cv2.drawKeypoints(img,kp,img_new)

cv2.imshow("FAST Feature Detection",img_new)
print(len(kp))
print(fast.getThreshold())
cv2.waitKey(0)
cv2.destroyAllWindows()

































