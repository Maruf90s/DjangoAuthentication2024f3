from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
def index(request):
    return render(request,"index.html")
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        newuser = User.objects.create_user(username=username,password=password)
        newuser.save()
        login(request,newuser)
        return redirect('SUC')
    return render(request,'signup.html')

def LOGIN_PRO(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect("SUC")
    return render(request,"login.html")
def success(request):
    if request.user.is_authenticated:
     if request.method == "POST":
         logout(request)
     return render(request,'success.html')
    
    else:
        return HttpResponse("You are not authenticated!")
    
        