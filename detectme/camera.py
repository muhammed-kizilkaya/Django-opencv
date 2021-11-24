 
from datetime import datetime, timedelta
import cv2
import os
import urllib.request
import numpy as np
from django.conf import settings
import time
global hrs
global mins
global secs
global totalsecs
 
from countdown import countdown


class VideoCamera_py(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()


    #This function is used in views
    def get_frame(self):
        success, image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frame_flip = cv2.flip(image, 1)
        ret, jpeg = cv2.imencode('.jpg', gray)
        return jpeg.tobytes() 
 