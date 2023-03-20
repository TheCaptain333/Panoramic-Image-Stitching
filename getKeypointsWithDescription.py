import numpy as np
import cv2
from getDetectorAndDescriptor import getDescriptor,getDetector
import argparse


def getKeypoints(img,detector):
    kp = detector.detect(img,None)
    return kp


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("detectorName")
    parser.add_argument("descriptorName")
    args=parser.parse_args()
    img = cv2.imread(args.filename,cv2.IMREAD_GRAYSCALE)
    detector=getDetector(args.detectorName)
    
    kp = getKeypoints(img,detector)
    print("Number of keypoints=",len(kp))
    
    






































