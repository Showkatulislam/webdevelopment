from django.shortcuts import render,HttpResponse
from .forms import Customerregistration
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def Registation(request):
    if request.method=='POST':
        fm=Customerregistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Done your Registration")
        return render(request,'Registation.html',{'form':fm})
    else:
        fm=Customerregistration()
        return render(request,'Registation.html',{'form':fm})
def Profile(request):
    return render(request,'profile.html')

