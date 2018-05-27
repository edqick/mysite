from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.views import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForms

# Create your views here.
def index(request):
    context = {}
    context['login_forms'] = LoginForms()
    return render(request,"index.html",context)

def register(request):
    return render(request,"register.html")

def tours(request):
    return render(request,"tours.html")

def hots(request):
    return render(request,"hots.html")

def blogs(request):
    return render(request,"blogs.html")

def contacts(request):
    return render(request,"contacts.html")

@csrf_exempt
def login_user(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("username : "+username)
        print("password : "+password)
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is None:
            print("账号或密码错误")
            return HttpResponse("fail")
        login(request,user)
        print("登入用户")
        return HttpResponse("success")
    return HttpResponse("fail")

@login_required(login_url="/home/")
def logout_user(request):
    logout(request)
    return HttpResponse("success")
