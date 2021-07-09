from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def checkAnonymous(request, template_name):
    if request.user.is_anonymous:
        return redirect('/login/')
    else:            
        return render(request, template_name)

        

def main(request):
    return checkAnonymous(request, 'index.html')



def shopCategory(request):
    return checkAnonymous(request, 'category.html')



def productDetails(request):
    return checkAnonymous(request, 'single-product.html')



def productCheckout(request):
    return checkAnonymous(request, 'checkout.html')



def shopingCart(request):
    return checkAnonymous(request, 'cart.html')



def confirmation(request):
    return checkAnonymous(request, 'confirmation.html')



def blog(request):
    return checkAnonymous(request, 'blog.html')


def blogDetails(request):
    return checkAnonymous(request, 'single-blog.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')


def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save() 
        return redirect('/login/')


    return render(request, 'signUp.html')


def tracking(request):
    return checkAnonymous(request, 'tracking.html')



def elements(request):
    return checkAnonymous(request, 'elements.html')


def contact(request):
    return checkAnonymous(request, 'contact.html')
