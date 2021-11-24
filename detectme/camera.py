 
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
 
 

class VideoCamera_py(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
        self.videoWriter = cv2.VideoWriter('video.avi', fourcc, 30.0, (640,480)) 
        self.hrs = 0
        self.mins = 10
        self.totalsecs = 3600 * self.hrs + 30 * self.mins  

    def __del__(self):
        self.video.release()


    #This function is used in views
    def get_frame(self):
        success, image = self.video.read()
        self.videoWriter.write(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frame_flip = cv2.flip(image, 1)
        ret, jpeg = cv2.imencode('.jpg', gray)
        cv2.putText(image, str(self.totalsecs), (70,70), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv2.LINE_AA)# adding timer text

        self.totalsecs -= 1
        if self.totalsecs == 0:
            return 

        return jpeg.tobytes() 
 
    