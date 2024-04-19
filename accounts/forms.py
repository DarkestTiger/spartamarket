from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
  
    
# 회원가입 폼
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    profile_img = forms.ImageField(label="프로필 사진")
    username = forms.CharField(label="아이디")
    password1 = forms.CharField(label="비밀번호1")
    password2 = forms.CharField(label="비밀번호2")

    class Meta:
        model = User
        fields = ("username","email","profile_img","password1","password2")

