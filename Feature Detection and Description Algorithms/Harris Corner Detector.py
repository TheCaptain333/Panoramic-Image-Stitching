import numpy as np
import cv2

filename = 'map1.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

dst=cv2.dilate(dst,None)

#threshold for an optimal value,may vary based on image

img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow("Harris Corners",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Optionally can implement subPixel accuracy





























