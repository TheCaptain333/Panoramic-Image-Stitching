import numpy as np
import cv2


filename = 'map1.jpg'

img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

star = cv2.xfeatures2d.StarDetector_create()

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()


kp=star.detect(img,None)

img_new = img
img_new = cv2.drawKeypoints(img,kp,img_new)


cv2.imshow("STAR Feature Detection",img_new)
print(len(kp))

cv2.waitKey(0)
cv2.destroyAllWindows()


_,des = brief.compute(img,kp)



























