from django.shortcuts import render, HttpResponse

# Create your views here.

def main(request):
    return render(request, 'index.html')


def shopCategory(request):
    return render(request, 'category.html')


def productDetails(request):
    return render(request, 'single-product.html')


def productCheckout(request):
    return render(request, 'checkout.html')


def shopingCart(request):
    return render(request, 'cart.html')


def confirmation(request):
    return render(request, 'confirmation.html')


def blog(request):
    return render(request, 'blog.html')


def blogDetails(request):
    return render(request, 'single-blog.html')


def login(request):
    return render(request, 'login.html')


def tracking(request):
    return render(request, 'tracking.html')


def elements(request):
    return render(request, 'elements.html')


def contact(request):
    return render(request, 'contact.html')