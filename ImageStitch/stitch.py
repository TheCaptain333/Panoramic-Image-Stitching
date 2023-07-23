import cv2
import numpy as np
from .models import Image
import os
from django.conf import settings

def MultipleImageStitching(image_path_list):
    #
    #
    dir = os.path.join(settings.MEDIA_ROOT,'images/')
    demo = cv2.imread(image_path_list[0])
    cv2.imwrite(os.path.join(dir,'demo.jpeg'),demo)
    final_object = Image()
    final_object.Images = 'images/demo.jpeg'
    final_object.save()
    return final_object


