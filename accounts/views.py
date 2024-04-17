from django.shortcuts import render, redirect
from accounts.forms import UserForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

# 회원가입 기능
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserForm()
    context = {"form": form}
    return render(request, "signup.html", context)

# 로그인 기능
class LoginView(View):
    template_name = 'signin.html'

    def get(self, request):
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            context = {'form':form}
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, self.template_name, context) 

# 로그아웃 기능

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')








