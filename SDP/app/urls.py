from .form import loginForm,customerregistration,MyPasswordChangeForm

from django.urls import path

from . views import home,RegistrarionView,search_results,Restaurent_detail_view,ProfileView,address,FoodAbout,AddCart,checkout,foodview,foodCategory

from django.contrib.auth import views as auth_view

urlpatterns = [
     path('',home,name="home"),


     path('registation/',RegistrarionView.as_view(),name="registation"),


     path('checkout/', checkout, name='checkout'),


     path('address/', address, name='address'),


     path('foodabout/',FoodAbout,name='foodabout'), 


     path('addcart/',AddCart,name='addcart'), 


     path('profile/',ProfileView.as_view(),name='profile'),


     path('login/',auth_view.LoginView.as_view(
     template_name='login.html',authentication_form=loginForm),name='login'),


     path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),


     path('passwordchangedone/',auth_view.PasswordChangeView.as_view
    (template_name='passwordchangedone.html',form_class=MyPasswordChangeForm,),name='passwordchangedone'),


     path('passwordchange/',auth_view.PasswordChangeView.as_view
    (template_name='passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),


     path('search/',search_results,name='search'),


     path('<pk>/',Restaurent_detail_view,name='resturant'),


     path('food/<int:pk>/',foodview,name='foodview'),

     path('foodcatagory/<str:pk>',foodCategory,name='foodcategory'),
]