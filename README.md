# Aerial-Survey-using-Drone
## Feature Matching  
**FeatureMatching.py** finds features in the two images and then finds corresponding points in the two images.  
Command:`python FeatureMatching.py source_image destination_image detectorName descriptorName`  
source_image = path to the first image  
destination_image = path to the second image  
detectorName  = feature detection algorithm to be used : SIFT,STAR,FAST,ORB  
descriptorName = feature descriptor algorithm to be used : SIFT,BRIEF,ORB  

## Image Stitching  
**ImageStitching.py** finds uses the matches found from FeatureMatching.py to compute the homography matrix, and transform one image relative to the other, generating the combined image  
Comand:`python ImageStitching.py source_image destination_image detectorName descriptorName`  
source_image = path to the first image  
destination_image = path to the second image  
detectorName  = feature detection algorithm to be used : SIFT,STAR,FAST,ORB  
descriptorName = feature descriptor algorithm to be used : SIFT,BRIEF,ORB  



