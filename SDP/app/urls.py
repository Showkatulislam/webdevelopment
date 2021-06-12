from .form import loginForm,customerregistration,MyPasswordChangeForm

from django.urls import path

from . views import home,RegistrarionView,search_results,Restaurent_detail_view,ProfileView,address,AddCart,checkout,foodview,foodCategory,ProductViewDetail,show_cart,plus_cart,minus_cart,remove_cart,Food,payment_done,order

from django.contrib.auth import views as auth_views

urlpatterns = [
     path('',home,name="home"),

     path('pluscart/',plus_cart),

     path('checkout/', checkout, name='checkout'),

     path('order/',order,name='orders'),

     path('minuscart/',minus_cart),

     path('removecart/',remove_cart),

     path('cart/',show_cart,name='showcart'),

     path('registation/',RegistrarionView.as_view(),name="registation"),


     path('paymentdone/',payment_done,name='paymentdone'),


     path('address/', address, name='address'),


     path('product-detail/<int:pk>', ProductViewDetail.as_view(), name='product-detail'),

     # path('foodabout/',FoodAbout,name='foodabout'), 


     path('addcart/',AddCart,name='addcart'), 


     path('profile/',ProfileView.as_view(),name='profile'),


     path('accounts/login/',auth_views.LoginView.as_view(
     template_name='login.html',authentication_form=loginForm),name='login'),


     path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),


     path('passwordchangedone/',auth_views.PasswordChangeView.as_view
    (template_name='passwordchangedone.html',form_class=MyPasswordChangeForm,),name='passwordchangedone'),


     path('passwordchange/',auth_views.PasswordChangeView.as_view
    (template_name='passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),


     path('foodview/',Food,name='foodview'),

     path('search/',search_results,name='search'),


     path('<pk>/',Restaurent_detail_view,name='resturant'),


     path('food/<int:pk>/',foodview,name='foodview'),

     path('foodcatagory/<str:pk>',foodCategory,name='foodcategory'),


]