# views.py

from django.shortcuts import render, get_object_or_404, HttpResponse
from .cart import Cart
from store.models import product  # Use lowercase 'product' to match the model name
from django.http import JsonResponse

def cart_summary(request):
    return render(request, 'cart/cart_summary.html')

def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('productid'))
        prod = get_object_or_404(product, id=product_id)  # Use lowercase 'product' to match the model name
        cart.add(product=prod)  # Changed 'prod' to 'product' to match the Cart.add method
        response = JsonResponse({'product_name': prod.name})
        return response
    else:
        return HttpResponse("Invalid request method")

def cart_delete(request):
    pass

def cart_update(request):
    pass
