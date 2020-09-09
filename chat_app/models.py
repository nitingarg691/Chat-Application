from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

User = get_user_model()
class Message(models.Model):
    author = models.ForeignKey(User,related_name = 'author_messages',on_delete = models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    roomname = models.CharField(max_length=40)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by('timestamp').all()

    def fetchRoomMessages(roomname):
        res = []
        messages = Message.objects.order_by('timestamp').all()
        for i in messages:
            if i.roomname == roomname:
                res.append(i)
        return res                



class UsersData(models.Model):
    username = models.CharField(max_length = 20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username 
