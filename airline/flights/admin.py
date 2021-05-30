from django.contrib import admin
from django.db.models.expressions import F
from .models import Airport,Flight,Passenger
# Register your models here.
@admin.register(Airport)
class airportModelAdmin(admin.ModelAdmin):
    list_display=['code','city']
@admin.register(Flight)
class FlightModelAdmin(admin.ModelAdmin):
    list_display=['origin','destination','duration']
@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display=['first','last']
