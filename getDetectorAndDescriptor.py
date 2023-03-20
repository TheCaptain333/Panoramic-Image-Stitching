import numpy as np
import cv2

def getDetector(name):
    if name == 'SIFT':
        sift = cv2.SIFT_create()
        return sift        
    elif name == 'STAR':
        star = cv2.xfeatures2d.StarDetector_create()
        return star
    
    elif name == 'FAST':
        fast = cv2.FastFeatureDetector_create()
        return fast
    
    elif name == 'ORB':
        orb = cv2.ORB_create()
        return orb
        
def getDescriptor(name):
    if name == 'SIFT':
        sift = cv2.SIFT_create()
        return sift        
    elif name == 'BRIEF':
        brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
        return brief
    elif name == 'ORB':
        orb = cv2.ORB_create()
        return orb
    
    






































