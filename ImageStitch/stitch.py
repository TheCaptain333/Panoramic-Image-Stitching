import cv2
import numpy as np
from .models import Image
import os
from django.conf import settings

orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

def getHomography(secondary_image,base_image):

    kp1,des1 = orb.detectAndCompute(secondary_image,None)
    kp2,des2 = orb.detectAndCompute(base_image,None)

    matches = bf.match(des1,des2)
    matches = sorted(matches, key = lambda x:x.distance)

    points_sec = np.zeros((len(matches),2),dtype=np.float32)
    points_base = np.zeros((len(matches),2),dtype=np.float32)
    
    for i,match in enumerate(matches):
        points_sec[i,:]=kp1[match.queryIdx].pt
        points_base[i,:]=kp2[match.trainIdx].pt

        src = points_sec.reshape(-1,1,2)
        des = points_base.reshape(-1,1,2)

    H,_ = cv2.findHomography(src,des,cv2.RANSAC,5.0)

    return H


def getTransformedImage(secondary_image,base_image):

    H = getHomography(secondary_image,base_image)
    
    (h1,w1) = base_image.shape
    (h2,w2) = secondary_image.shape
    initial_matrix = np.array([[0,w2-1,w2-1,0],[0,0,h2-1,h2-1],[1,1,1,1]])
    final_matrix = np.dot(H,initial_matrix)
    [x,y,c] = final_matrix
    x = np.divide(x,c)
    y = np.divide(y,c)

    min_x , max_x = int(round(min(x))),int(round(max(x)))
    min_y , max_y = int(round(min(y))),int(round(max(y)))

    height_correction,width_correction = 0,0

    if(min_x < 0): 
        width_correction = abs(min_x)
    if(min_y < 0): 
        height_correction = abs(min_y)

    new_width = max_x + width_correction
    new_height = max_y + height_correction

    if(new_width < w1 + width_correction):
        new_width = w1 + width_correction
    if(new_height < h1 + height_correction):
        new_height = h1 + height_correction

    old_initial_points = np.float32([[0,0],[w2-1,0],[w2-1,h2-1],[0,h2-1]])
    x = x + width_correction
    y = y + height_correction

    new_final_points = np.float32(np.array([x,y]).transpose())
    

    updated_H = cv2.getPerspectiveTransform(old_initial_points,new_final_points)

    StitchedImage = cv2.warpPerspective(secondary_image,updated_H,(new_width,new_height))
    new_copy = np.copy(StitchedImage)
    StitchedImage[height_correction:height_correction+h1,width_correction:width_correction+w1] = base_image
    final_image = cv2.addWeighted(new_copy,0.5,StitchedImage,0.5,0)
    return final_image



def MultipleImageStitching(image_path_list):
    #
    #
    dir = os.path.join(settings.MEDIA_ROOT,'images/')
    

    base_image = cv2.imread(image_path_list[0],0)

    for i in range(1,len(image_path_list)):
        secondary_image = cv2.imread(image_path_list[i],0)
        base_image = getTransformedImage(secondary_image,base_image)

    cv2.imwrite(os.path.join(dir,'output.jpeg'),base_image)
    final_object = Image()
    final_object.Images = 'images/output.jpeg'
    final_object.save()
    return final_object


