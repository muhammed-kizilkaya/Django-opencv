from imutils.video import VideoStream
import imutils
import cv2
import os
import urllib.request
import numpy as np
from django.conf import settings





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

class camera_record(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()


    #This function is used in views
    def get_frame(self):

        success, image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        frame_flip =cv2.putText(image, "Her iyilik/guzel is bir sadakadir", (1, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (39, 32, 224),2)

        ret, jpeg = cv2.imencode('.jpg', frame_flip)
        
        return jpeg.tobytes()



class IPWebCam(object):
    def __init__(self):
        self.url = "http://127.0.0.1:8000/video_feed"


    def __del__(self):
        cv2.destroyAllWindows()

    def get_frame(self):
        imgResp = urllib.request.urlopen(self.url)
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
        img = cv2.imdecode(imgNp, -1)
        img =cv2.resize(img, (640, 480))
        frame_flip = cv2.flip(img, 1)
        ret, jpeg = cv2.imencode('.jpg', frame_flip)
        return jpeg.tobytes()