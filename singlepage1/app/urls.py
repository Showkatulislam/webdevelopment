from django.urls import path
from .views import view,section
urlpatterns=[
    path('',view),
    path('section/<int:num>',section),
]