from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    data = log.objects.get(id = 1)
    fundsdata = fund.objects.all()
    context = {
        'data':data,
        'fundsdata':fundsdata
    }
    load = loader.get_template('charity.html')
    return HttpResponse(load.render(context,request))

def fundraiser(request):
    load = log.objects.get(id =1)
    if load.signins:
        template=loader.get_template('main.html')
        return HttpResponse(template.render({},request))
    return redirect('login')
def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render({},request))

def signup(request):
    template=loader.get_template('signup.html')
    return HttpResponse(template.render({},request))
def back(request):
    return redirect('login')
def createuser(request):
    users = request.POST['username']
    password1 = request.POST['password1']
    email = request.POST['email']
    password2= request.POST['password2']

    if password1 == password2:
        load = user(username = users,password1 = password1,email = email)
        load.save()
        return redirect('login')
    else:
        return HttpResponse("pasword are not match")
    
def signin(request):
    email = request.POST['emailid']
    password = request.POST['pass']
    data = user.objects.filter(email = email)
    if data:
        data = user.objects.get(email=email)
        if data.password1 == password:
            load = log.objects.get(id=1)
            load.signins = True
            load.username = data.username
            load.emailid = email
            load.save()   
            return redirect('index')
        else:
            return HttpResponse("Incorect password")
    else:
        return HttpResponse("user name not found")
def logout(request):
    load = log.objects.get(id=1)
    load.signins = False
    load.save()
    return redirect('index')

def add(request):
    load = log.objects.get(id = 1)
    raiser = load.username
    name=request.POST["uname"]
    goal=request.POST["mygoal"]
    messages=request.POST["messages"]
    image=request.FILES["photos"]
    load=fund(username=name,goal=goal,message=messages,image=image)
    load.save()
    return redirect('index')

