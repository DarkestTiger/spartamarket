from django.db import models
from django.contrib.auth.models import AbstractUser


# 유저 모델
class User(AbstractUser):    
    profile_img = models.ImageField(blank=True, upload_to='profile_img/%Y/%m/%d/')
    follower = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="followers")
    
    
    def image_uploader(instance,filename):
        return f'user_{instance.pk}/{filename}'