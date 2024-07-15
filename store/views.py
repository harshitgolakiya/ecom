from django.shortcuts import render,redirect
from .models import product,category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .forms import signup_form


# Create your views here.
def products(request):
    products = product.objects.all()
    categories = category.objects.all() 
    context = {
    'products': products,
    'categories': categories,
    }
    return render(request, 'store/products.html', context)
    # return render(request, 'store/products.html', {'products': products}, {'categories': categories})

def loginuser(request):
    if request.user.is_authenticated:
        return products(request)
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ("You have been logged in"))
                return products(request)
            else:
                messages.success(request, ("There was an error logging in, try again"))
                return render(request, 'store/login.html')
        else:
            return render(request, 'store/login.html')

def logoutuser(request):
    logout(request)
    messages.success(request, ("You have been logged out..."))
    return products(request)

def register(request):
    if request.user.is_authenticated:
        return redirect('products')
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successful!"))
            return redirect('products')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = signup_form()
    return render(request, 'store/register.html', {'form': form})

def product_info(request, product_id):
    pinfo = product.objects.get(id=product_id)
    return render(request, 'store/product_info.html', {'pinfo': pinfo})

#to filter products by specific category
def product_category(request, category_name):
    products = product.objects.filter(category__name=category_name)
    categories = category.objects.all()
    if products:
        context = {
        'products': products,
        'categories': categories,
        }
        return render(request, 'store/products.html', context)
    else:
        messages.error(request, 'No products available in this category')
        return redirect('products')