from typing import ValuesView
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from main import views

urlpatterns = [
    path('', views.main, name='home'),
    path('shop-category/', views.shopCategory, name='shop-category'),
    path('product-details/', views.productDetails, name='product-details'),
    path('product-checkout/', views.productCheckout, name='product-checkout'),
    path('shopping-cart/', views.shopingCart, name='shopping-cart'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blogDetails, name='blog-details'),
    path('login/', views.login, name='login'),
    path('tracking/', views.tracking, name='tracking'),
    path('elements/', views.elements, name='elements'),
    path('contact/', views.contact, name='contact'),
]