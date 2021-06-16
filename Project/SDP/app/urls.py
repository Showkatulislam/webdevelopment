
from django import forms
import django
from django.urls import path

from . views import home,Registation,Profile

from . forms import LoginForm

from django.contrib.auth import views

urlpatterns = [
     path('',home,name="home"),
     path('registation/',Registation,name="registation"),
     path('login/',views.LoginView.as_view(
     template_name='login.html',authentication_form=LoginForm),name='login'),
     path('profile/',Profile,name='profile'),
     path('logout/',views.LogoutView.as_view(next_page='login'),name='logout'),
       
]