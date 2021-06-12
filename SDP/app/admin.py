from django.contrib import admin
from .models import Restaurant,Bannerslide,Customer,ResFood,Cart,OrderPlaced
# Register your models here.


####This is Section for Restaurent admin Table###########
@admin.register(Restaurant)
class restaurentAdmin(admin.ModelAdmin):
    list_display=['id','name','restaurant_id','area']


####This is Section for Banner Admin form Table###########
@admin.register(Bannerslide)
class bannrAdmin(admin.ModelAdmin):
    list_display=['id','restaurant_id','image']


####This is Section for Customer Address Admin Table##########
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','name','locality','zipcode','upazila','city']

admin.site.register(ResFood)


admin.site.register(Cart)

admin.site.register(OrderPlaced)

