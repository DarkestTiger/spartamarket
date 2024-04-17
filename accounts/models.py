from django.db import models
from django.contrib.auth.models import AbstractUser


# 유저 모델
class User(AbstractUser):    
    profile_img = models.ImageField(blank=True, upload_to='profile_img//%Y/%m/%d/')