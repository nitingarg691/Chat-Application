
from django.contrib import admin
from .views import index
from django.conf.urls import url
from . import views
from django.urls import path,re_path

app_name = 'chat_app'

urlpatterns = [
    path('<str:room_name>/',views.room,name='room'),
]
