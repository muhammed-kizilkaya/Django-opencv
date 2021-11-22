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

    def __str__(self) -> str:
        return f"{self.header}"

 