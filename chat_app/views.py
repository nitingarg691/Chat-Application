from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.views.generic import DetailView,CreateView
import json
from chat_app.models import UsersData

from django.urls import reverse_lazy
from django.contrib.auth import login as d_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def room(request):
    user_data = UsersData.objects.all()
    print("logging in")
    return render(request, 'room.html', {
        'room_name': "hey",
        'username' : request.user.username,
        'userdata':user_data
    })

def signUp(request):
    return render(request,'signup.html')


def postLogin(request):
    if request.method == 'POST':
        userName = request.POST['username']
        passWord = request.POST['password']
 
        user = authenticate(request,username=userName,password=passWord)
        print(user)
        if user is not None:
            d_login(request,user)
            user_data = UsersData.objects.all()
            print("logging in")
            return render(request,'room.html',{
                'room_name':'aman',
                 'username' : user,
                 'userdata':user_data,
            })
           
        else:
            return HttpResponse("Invalid Details")


def postSignUp(request):
    if request.method == "POST":
        userName = request.POST['username']
        Email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        User.objects.create_user(username = userName,password = password,email=Email)
        UsersData.objects.create(username=userName,email=Email,password=password,gender=gender)
        print("User created")
        return render(request,'login.html')
