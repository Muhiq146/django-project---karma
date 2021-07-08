from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index.html/', views.ind, name='index'),
    path('blog.html/', views.blog, name='index'),
    path('cart.html/', views.cart, name='index'),
    path('category.html', views.cat, name='category'),
    path('checkout.html/', views.check, name='index'),
    path('confirmation.html/', views.conf, name='index'),
    path('contact.html/', views.con, name='contact'),
    path('elements.html/', views.ele, name='index'),
    path('login.html/', views.log, name='index'),
    path('single-blog.html/', views.sib, name='single-blog'),
    path('single-product.html/', views.sip, name='index'),
    path('tracking.html/', views.track, name='index'),
]