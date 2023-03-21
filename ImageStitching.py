import numpy as np
import cv2
import argparse
from FeatureMatching import getMatches

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
    
    
    
    src_img = cv2.resize(src_img,(src_img.shape[1]*400//src_img.shape[0],400))
    dest_img = cv2.resize(dest_img,(dest_img.shape[1]*400//dest_img.shape[0],400))
    
    if(len(arg_dict)==2):
        arg_dict['detectorName']='ORB'
        arg_dict['descriptorName']='ORB'
    elif(len(arg_dict)==3):
        arg_dict['descriptorName']='ORB'
        
    kp1,kp2,matches = getMatches(arg_dict["detectorName"],arg_dict["descriptorName"],src_img,dest_img)
    
    src_points = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1,1,2)
    dest_points = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1,1,2)       
            
    M,mask = cv2.findHomography(dest_points,src_points,cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()

    width=dest_img.shape[1]+src_img.shape[1]
    height=dest_img.shape[0]+src_img.shape[0]

    result = cv2.warpPerspective(dest_img,M,(width,height))
    result[0:src_img.shape[0],0:src_img.shape[1]]=src_img
    
    cv2.imshow("Image 1",src_img)
    cv2.imshow("Image 2",dest_img)
    cv2.imshow("Final Image",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
    
    





































