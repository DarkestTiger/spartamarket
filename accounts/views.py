from django.shortcuts import render, redirect
from accounts.forms import UserForm 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from accounts.models import User


# 회원가입 기능
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            auth_login(request, user)
            return redirect("home")
    else:
        form = UserForm()
    context = {"form": form}
    return render(request, "signup.html", context)

# 로그인 기능
def login(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("spartamarket:home")
    else:
        form = UserForm()
    context = {"form": form}
    return render(request, "signin.html", context)
  
# 로그아웃 기능

def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect("index")








