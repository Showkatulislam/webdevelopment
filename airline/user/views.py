from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,"user/index.html")



def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"user/login.html",{'text':
            'login Fail try again,please!!!'})

    return render(request,"user/login.html")


def Logout(request):
    logout(request)
    return render(request,"user/login.html",
    {'text':"login please"}
    )
