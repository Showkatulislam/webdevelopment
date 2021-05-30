from django.urls import path
from .views import index,Login,Logout
urlpatterns=[
    path("",index,name='index'),
    path("login/",Login,name='login'),
    path("logout/",Logout,name='logout'),
]
