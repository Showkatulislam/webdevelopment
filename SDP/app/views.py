from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse
from .models import Restaurant,Bannerslide,Customer,ResFood
from django.views import View
from .form import customerregistration,CustomerProfileForm
from django.contrib import messages
# Create your views here.


####This is Section for Home view ###########
def home(request):
    rest=Restaurant.objects.all()
    return render(request,'home.html',{'rest':rest})


####This is Section for Customer registration view ###########
class RegistrarionView(View):
    def get(self,request):
        form=customerregistration()
        return render(request,'customerregistation.html',{'form':form})
    def post(self,request):
        form=customerregistration(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation!!!')
            form.save()
        return render(request,'customerregistation.html',{'form':form})


####This is Section for Profile view Table###########
def Profile(request):
   return render(request,'profile.html')


####This is Section for Restaurent View Table###########
def Restaurent_detail_view(request,pk):
    nam=Restaurant.objects.filter(restaurant_id__icontains=pk)
    rest=nam[0].name
    banner=Bannerslide.objects.filter(restaurant_id__icontains=pk)
    ban=Bannerslide.objects.filter(restaurant_id__icontains=101)
    id=Restaurant.objects.get(restaurant_id__icontains=pk)
    food=ResFood.objects.filter(restaurent_id=id)
    if banner==0:
        bn1=banner[0]
        bn2=banner[1]
        bn3=banner[2]
        return render(request,'Restaurent_view.html',{'bn1':bn1,'bn2':bn2,'bn3':bn3,'rest':rest,'food':food})
    else:
        bn1=ban[0]
        bn2=ban[1]
        bn3=ban[2]
        return render(request,'Restaurent_view.html',{'bn1':bn1,'bn2':bn2,'bn3':bn3,'rest':rest,'food':food})


####This is Section for search ajax function ###########
def search_results(request):
    if request.is_ajax():
        res=None
        game=request.POST.get('game')
        qs=Restaurant.objects.filter(area__icontains=game)
        if len(qs)>0 and len(game)>0:
            data=[]
            for pos in qs:
                item={
                    'pk':pos.restaurant_id,
                    'name':pos.name,
                    'area':pos.area,
                    'image':str(pos.image.url)
                },
                data.append(item)
            res=data
        else:
            res='RESTAURENT NOT FOUND.'
        return JsonResponse({'data':res})
    return JsonResponse({})

####This is Section for Customer Address view Table###########
class ProfileView(View):
     def get(self,request):
         form=CustomerProfileForm()
         return render(request,'profile.html',{'form':form})
     def post(self,request):
         form=CustomerProfileForm(request.POST)
         if form.is_valid():
             usr=request.user
             name=form.cleaned_data['name']
             locality=form.cleaned_data['locality']
             zipcode=form.cleaned_data['zipcode']
             upazila=form.cleaned_data['upazila']
             city=form.cleaned_data['city']
             reg=Customer(user=usr,name=name,locality=locality,zipcode=zipcode,upazila=upazila, city= city)
             reg.save()
             messages.success(request,'congratulations !! Update Successfully')
         return render(request,'profile.html',{'form':form})

def address(request):
    if request.user.is_authenticated:
        add=Customer.objects.filter(user=request.user)
        return render(request,'address.html',{'add':add,'active':'btn-info'})
    else:
        add=''
        return render(request,'address.html',{'add':add,'active':'btn-info'})


def FoodAbout(request):
    return render(request,'food_about.html')

def AddCart(request):
    return render(request,'add_cart.html')

def checkout(request):
    if request.user.is_authenticated:
        add=Customer.objects.filter(user=request.user)
        return render(request, 'checkout.html',{'add':add})
    else:
        add=''
        return render(request, 'checkout.html',{'add':add})


def foodview(request,pk):
    return HttpResponseRedirect('/')


def foodCategory(request,data):
    if data=='P':
         food=ResFood.objects.filter(category='P')
         print(food)
    elif data=='KB':
        food=ResFood.objects.filter(category='KB')
    elif data=='BK':
        food=ResFood.objects.filter(category='BK')
    elif data=='MP':
        food=ResFood.objects.filter(category='MP')
    elif data=='RC':
        food=ResFood.objects.filter(category='RC')
    return render(request,'food_category.html',{'food':food})