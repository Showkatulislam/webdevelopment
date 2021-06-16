from django.urls import path
from .views import *
urlpatterns=[
    path('',main_view,name='main-view'),
    path('rate/',rate_view,name='rate-view')
]