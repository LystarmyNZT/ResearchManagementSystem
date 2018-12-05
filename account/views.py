from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import auth_logout
from .forms import LoginForm,RegsterForm
# Create your views here.

def userLogin(request):
    if request.method=="POST":
        loginFm=LoginForm(request.POST)
        if loginFm.is_valid():
            cd=loginFm.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(request,user)
                return render(request,"REAccount/success.html")
            else:
                return render(request,"REAccount/failure.html")
        else:
            return HttpResponse("Invalid login")

    if request.method=="GET":
        loginFm=LoginForm()
        return render(request,"REAccount/login.html",{"form":loginFm})

def userRegister(request):
    if request.method=="POST":
        userForm=RegsterForm(request.POST)
        if userForm.is_valid():
            new_user=userForm.save(commit=False)
            new_user.set_password(userForm.cleaned_data['password'])
            new_user.save()
            return render(request,"REAccount/success.html")
        else:
            return render(request,"REAccount/failure.html")
    else:
        userForm=RegsterForm()
        return  render(request,"REAccount/register.html",{"form":userForm})

def logout(request):
    auth_logout(request)
    return render(request,"REAccount/logout.html")