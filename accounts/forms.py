from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
  
    
# 회원가입 폼
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username","email","profile_img")