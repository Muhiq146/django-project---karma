"""karma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('index.html/', include('main.urls')),
    path('blog.html/', include('main.urls')),
    path('cart.html/', include('main.urls')),
    path('category.html/', include('main.urls')),
    path('checkout.html/', include('main.urls')),
    path('confirmation.html/', include('main.urls')),
    path('contact.html/', include('main.urls')),
    path('elements.html/', include('main.urls')),
    path('login.html/', include('main.urls')),
    path('single-blog.html/', include('main.urls')),
    path('single-product.html/', include('main.urls')),
    path('tracking.html/', include('main.urls')),
]
