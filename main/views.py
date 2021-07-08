from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ind(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def cat(request):
    return render(request, 'category.html')

def check(request):
    return render(request, 'checkout.html')

def conf(request):
    return render(request, 'confirmation.html')

def con(request):
    return render(request, 'contact.html')

def ele(request):
    return render(request, 'elements.html')

def log(request):
    return render(request, 'login.html')

def sib(request):
    return render(request, 'single-blog.html')

def sip(request):
    return render(request, 'single-product.html')

def track(request):
    return render(request, 'tracking.html')
