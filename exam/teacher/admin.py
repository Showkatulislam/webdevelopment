from django.contrib import admin
from .models import Teacher
# Register your models here.
@admin.register(Teacher)
class SAdmin(admin.ModelAdmin):
    list_display=['user']
