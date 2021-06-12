
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
# Create your models here.


####This is Section for Restaurent database Table###########
class Restaurant(models.Model):
    name=models.CharField(max_length=50)
    restaurant_id=models.IntegerField(unique=True,null=False)
    area=models.CharField(null=False, max_length=50)
    image=models.ImageField(upload_to='restaurent')
    def __str__(self):
        return str(self.restaurant_id)


####This is Section for banner database Table###########
class Bannerslide(models.Model):
    restaurant_id=models.IntegerField(null=False)
    image=models.ImageField(upload_to='banner')


####This is Section for Customer Address database Table###########
choose=(
    ('Chittagong','SATAKNIA'),
    ('Chittagong','ANOWARA'),
    ('Chittagong','BOALKHALI'),
    ('Chittagong','CHANDANAISH'),
    ('Chittagong','HATHAZARI'),
    ('Chittagong','MIRSHARAI'),
    ('Chittagong','PATIYA'),
    ('Chittagong','RANGUNIA'),
    ('Chittagong','SANDWIP'),
    ('Chittagong','BOALKHAL'),
)
citychoose=(
     ('C','Chittagong'),
     ('D','Dhaka'),
     ('Co','Comilla'),
     ('Ch','Chandpur'),
     ('S','Sylhet'),
     ('C','Coxs bazer'),
     ('B','Bandarban'),
)
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    zipcode=models.IntegerField()
    upazila=models.CharField(choices=choose,max_length=50)
    city=models.CharField(choices=citychoose,max_length=200)
    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES=(
    ('Bf','Beaf_fry'),
    ('Fi','Fish'),
    ('Ch','Chicken'),
    ('C','chamuca'),
    ('B','Biryani'),
    ('P','Paratha'),
    ('KB','Kachchi Biryani'),
    ('BK','Bhuna Khichuri'),
    ('MP','Morog Polao'),
    ('RC','Rice with Curry and vaji'),
    ('GC','Grilled Chicken'),
    ('H','Haleem'),
    ('SK','Sheek Kabab'),
    ('PO','Fuchka'),
    ('MD','Misti Doi'),
    ('DC','Doi Chira'),
    ('FD','Falooda'),
    ('RM','Rasmali'),
    ('BH','Borhani'),
    ('SL','Sweet Lassi'),
)
class ResFood(models.Model):
    restaurent_id=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    food_title=models.CharField(max_length=55)
    description=models.CharField(max_length=200)
    food_price=models.IntegerField()
    dicount_price=models.IntegerField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    food_image=models.ImageField(upload_to='Food_image')
    def __str__(self) -> str:
        return str(f"{self.restaurent_id} {self.id} {self.food_title}")

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food=models.ForeignKey(ResFood,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(f"{self.user} {self.id}")
    @property
    def total_cost(self):
        return self.quantity*self.food.food_price
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    resturant_id=ForeignKey(Restaurant,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    food=models.ForeignKey(ResFood,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,
    choices=STATUS_CHOICES,default='Pendeing')
    @property
    def total_cost(self):
        return self.quantity*self.food.food_price


