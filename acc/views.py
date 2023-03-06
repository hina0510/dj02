from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages
# Create your views here.

def update(request):
    if request.method == "POST":
        u = request.user
        uc = request.POST.get("ucomm")
        um = request.POST.get("umail")
        pi = request.FILES.get("upic")
        u.email , u.comment = um, uc
        if pi:
            u.pic.delete()
            u.pic = pi
        u.save()
        return redirect("acc:profile")
    return render(request, "acc/update.html")

def chpass(request):
    u = request.user
    cp = request.POST.get("cpass")
    if check_password(cp, u.password):
        np = request.POST.get("npass")
        u.set_password(np)
        u.save()
        return redirect("acc:login")
    return redirect("acc:update")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        ua = request.POST.get("uage")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        try:
            User.objects.create_user(username=un, password=up, age=ua, comment=uc, pic=pi)
            return redirect("acc:login")
        except:
            messages.info(request, "정보를 기입해주세요")
    return render(request, "acc/signup.html")

def delete(request):
    u = request.user
    up = request.POST.get("upass")
    if check_password(up, u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    else:
        messages.error(request, "패스워드를 확인해주세요")
    return redirect("acc:profile")
    

def profile(request):
    return render(request, "acc/profile.html")

def ulogout(request):
    logout(request)
    messages.success(request, "로그아웃되셨습니다")
    return redirect("acc:index")

def index(request):
    d = {1:"one", 2:"two", 3:"three"}
    context = {
        "d" : d
    }
    return render(request, "acc/index.html", context)

def ulogin(request):

    if request.user.is_authenticated:
        return redirect("acc:index")

    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            messages.success(request, f" {u} 님 환영합니다!")
            return redirect("acc:index")
        else:
            messages.info(request, "계정정보가 일치하지 않습니다")
    return render(request, "acc/login.html")

