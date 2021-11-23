from typing import Reversible
from django.db import models
from django.db.models.query_utils import select_related_descend
from django.shortcuts import redirect

from detectme.camera import VideoCamera_py



# Create your models here.
class UserEntry(models.Model):
    Rating = [
     
    ('Video', 'Video'),
    ('test', 'Test')
]
    header = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length = 15, choices = Rating)
    cevap_a= models.CharField(max_length=150,verbose_name="Şık A",default="Lorem İpsum A")
    cevap_b= models.CharField(max_length=150,verbose_name="Şık B",default="Lorem İpsum B")
    cevap_c= models.CharField(max_length=150,verbose_name="Şık C",default="Lorem İpsum C")
    cevap_d= models.CharField(max_length=150,verbose_name="Şık D",default="Lorem İpsum D")
    cevap_e= models.CharField(max_length=150,verbose_name="Şık E",default="Lorem İpsum E")


    def __str__(self) -> str:
        return f"{self.header}"

 