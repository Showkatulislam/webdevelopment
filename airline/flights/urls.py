from django.urls import path
from .views import index,flight,Book
urlpatterns=[
    path('',index,name='index'),
    path('<int:flight_id>',flight,name='flight'),
    path('<int:flight_id>/book',Book,name='book')
]