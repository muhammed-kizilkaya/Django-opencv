from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cv2_page', views.cv2_page, name="cv2-page"),
    path('auto_record', views.auto_record, name="auto_record"),
    path('detectme', views.detectme, name="detectme"),
    ]