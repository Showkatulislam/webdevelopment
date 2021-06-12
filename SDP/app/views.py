import json
from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import JsonResponse
from .models import Cart, Restaurant,Bannerslide,Customer,ResFood,OrderPlaced
from django.views import View
from .form import customerregistration,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


####This is Section for Home view ###########
def home(request):
    rest=Restaurant.objects.all()
    return render(request,'home.html',{'rest':rest})
def order(request):
    of=OrderPlaced.objects.filter(user=request.user)
    return render(request,'order.html',{'order':of})


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
    # nam=Restaurant.objects.filter(restaurant_id__icontains=pk)
    # rest=nam[0].name
    nam=Restaurant.objects.get(restaurant_id=pk)
    rest=nam
    banner=Bannerslide.objects.filter(restaurant_id__icontains=pk)
    ban=Bannerslide.objects.filter(restaurant_id__icontains=101)
    id=Restaurant.objects.get(restaurant_id__icontains=pk)
    food=ResFood.objects.filter(restaurent_id=id)
    if banner:
        bn1=banner[0]
        bn2=banner[1]
        bn3=banner[2]
        return render(request,'Restaurent_view.html',{'bn1':bn1,'bn2':bn2,'bn3':bn3,'rest':rest.name,'food':food})
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
@method_decorator(login_required,name='dispatch')
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

# def FoodAbout(request):
#     return render(request,'food_about.html')

def AddCart(request):
    user=request.user
    id=request.GET.get('food_id')
    food=ResFood.objects.get(id=id)
    cart=Cart.objects.filter()
    Cart(user=user,food=food).save()
    return redirect('/cart')


@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=40.
        total_amount=0
        cart_food=[f for f in Cart.objects.all() if f.user==user]
        if cart_food:
            for f in cart_food:
              tempamount=(f.quantity*f.food.food_price)
              amount+=tempamount
              total_amount=amount+shipping_amount
        return render(request,'add_cart.html',{'cart':cart,'totalamount':total_amount,'amount':amount})
    else:
        return render(request,'add_cart.html')

@login_required
def checkout(request):
    if request.user.is_authenticated:
        add=Customer.objects.filter(user=request.user)
        cart_items=Cart.objects.filter(user=request.user)
        amount=0.0
        shipping_amount=40.0
        total_amount=0.0
        cart_food=[f for f in Cart.objects.all() if f.user==request.user]
        if cart_food:
            for f in cart_food:
                tempamount=(f.quantity*f.food.food_price)
                amount+=tempamount
            total_amount=amount+shipping_amount
        return render(request, 'checkout.html',{'add':add,'cartitem':cart_items,'total_amount':total_amount})
    else:
        add=''
        return render(request, 'checkout.html',{'add':add})


login_required(login_url='login')
def payment_done(request):
    user=request.user
    custid=request.GET.get('custid')
    customer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    print(cart)
    for c in cart:
        OrderPlaced(resturant_id=c.food.restaurent_id,user=user,customer=customer,food=c.food,quantity=c.quantity).save()
        c.delete()
    return redirect('orders')
    


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


class ProductViewDetail(View):
    def get(self,request,pk):
        product=ResFood.objects.get(pk=pk)
        return render(request,'food_about.html',{'food':product})


def plus_cart(request):
    if request.method=='GET': 
        food_id=request.GET['prod_id']
        print(food_id )
        user=request.user
        c=Cart.objects.get(Q(food=food_id) & Q(user=user))
        c.quantity+=1
        c.save()
        amount=0.0
        total_amount=0
        shipping_amount=40.
        cart_food=[f for f in Cart.objects.all() if f.user==user]
        for f in cart_food:
            tempamount=(f.quantity*f.food.food_price)
            amount+=tempamount
            total_amount=amount+shipping_amount
            data={
                  'quantity':c.quantity,
                  'amount':amount,
                  'tototamount':total_amount
              }
    return JsonResponse(data)


def minus_cart(request):
    if request.method=='GET': 
        food_id=request.GET['prod_id']
        print(food_id )
        user=request.user
        c=Cart.objects.get(Q(food=food_id) & Q(user=user))
        c.quantity-=1
        c.save()
        amount=0.0
        total_amount=0
        shipping_amount=40.
        cart_food=[f for f in Cart.objects.all() if f.user==user]
        for f in cart_food:
            tempamount=(f.quantity*f.food.food_price)
            amount+=tempamount
            total_amount=amount+shipping_amount
            data={
                  'quantity':c.quantity,
                  'amount':amount,
                  'tototamount':total_amount
              }
    return JsonResponse(data)

def remove_cart(request):
    if request.method=='GET':
        food_id=request.GET['prod_id']
        user=request.user
        c=Cart.objects.get(Q(food=food_id) & Q(user=user))
        c.delete()
        amount=0.0
        total_amount=0
        shipping_amount=40.
        cart_food=[f for f in Cart.objects.all() if f.user==user]
        for f in cart_food:
            tempamount=(f.quantity*f.food.food_price)
            amount+=tempamount
            data={
                  'amount':amount,
                  'tototamount':amount+shipping_amount
              }
    return JsonResponse(data)


def Food(request):
    B=ResFood.objects.filter(category='B')
    Fi=ResFood.objects.filter(category='Fi')
    Ch=ResFood.objects.filter(category='Ch')
    C=ResFood.objects.filter(category='C')

    context={
        'B':B,
        'Fi':Fi,
        'Ch':Ch,
        'C':C,
    }
    return render(request,'food.html',context)

