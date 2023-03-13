from django.shortcuts import render
from products.models import Product

def home_page(request):

    object = Product.objects.all()
    context = {
        'object': object
    }
    
    return render(request, 'home.html', context)

def product_page(request, slug):

    object = Product.objects.get(slug=slug)
    context = {
        'obj': object
    }

    return render(request, 'product.html', context )