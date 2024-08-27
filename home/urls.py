from django.contrib import admin
from django.urls import path
from home.views import *
from home import views


urlpatterns = [
    path("admin/" , admin.site.urls),
    path('', index),
    path("home/", home , name="home"),
    path("about/", about , name="about"),
    path("service/", service , name="service"),
    path("menu/", menu , name="menu"),
    path("recepie/", recepie , name="recepie"),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
    path("booktable/", booktable , name="booktable"),
    path('signup',views.handleSignup, name='handleSignup'),
    path('login',views.handleLogin, name='handleLogin'),
    path('logout',views.handleLogout, name='handeLogin'),
    path('profile',views.profile,name='profile'),
    path('onlne_order',views.onlineorder,name='onlineorder'),
    path('add-cart/<dish_uid>/' , views.add_cart , name='add_cart'),
    path('cart', views.cart ,name='cart'),
    path('remove_cart_items/<cart_item_uid>/' , remove_cart_items , name='remove_cart_items')



]