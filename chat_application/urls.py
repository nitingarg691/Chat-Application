
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from chat_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup',views.signUp,name='signup'),
    path('admin/', admin.site.urls),
    url('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    path('',views.room,name='room'),
    path('postlogin',views.postLogin,name='postlogin'),
    path('postsignup',views.postSignUp,name='postsignup'),
    path('chat/',include('chat_app.urls',namespace='chat_app')),

]
