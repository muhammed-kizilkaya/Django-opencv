from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cv2_page', views.cv2_page, name="cv2-page"),
    path('auto_record', views.auto_record, name="auto_record"),
    path('detectme', views.detectme, name="detectme"),
    path('video_feed', views.video_feed, name='video_feed'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    path('list_questions', views.list_questions, name='list_questions'),
    
    ]