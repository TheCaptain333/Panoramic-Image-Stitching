import numpy as np
import cv2
from getDetectorAndDescriptor import getDescriptor,getDetector
import argparse


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("source_image")
    parser.add_argument("destination_image")
    parser.add_argument("detectorName")
    parser.add_argument("descriptorName")
    args=parser.parse_args()
    arg_dict = vars(args)
    
    src_img = cv2.imread(args.source_image,cv2.IMREAD_GRAYSCALE)
    dest_img = cv2.imread(args.destination_image,cv2.IMREAD_GRAYSCALE)
    
    if(len(arg_dict)==2):
        arg_dict['detectorName']='ORB'
        arg_dict['descriptorName']='ORB'
    elif(len(arg_dict)==3):
        arg_dict['descriptorName']='ORB'
        
    kp1 = getDetector(arg_dict["detectorName"]).detect(src_img,None)
    kp2 = getDetector(arg_dict["detectorName"]).detect(dest_img,None)
    _,des1 = getDescriptor(arg_dict["descriptorName"]).compute(src_img,kp1)
    _,des2 = getDescriptor(arg_dict["descriptorName"]).compute(dest_img,kp2)
    
    flag = 0
    if(arg_dict["descriptorName"]=='ORB'or arg_dict["descriptorName"]=='BRIEF'):
        flag = cv2.NORM_HAMMING
    elif(arg_dict["descriptorName"]=='SIFT'):
        flag = cv2.NORM_L2
   
    bf = cv2.BFMatcher(flag,crossCheck=True)
    matches = bf.match(des1,des2)
    matches = sorted(matches, key = lambda x:x.distance)
    img3 = cv2.drawMatches(src_img,kp1,dest_img,kp2,matches[0:50],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imshow("Brute-Force Matching",img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    





































