from django.shortcuts import render, get_object_or_404
from products.models import Product
from cart.models import Cart


def home_page(request):

    object = Product.objects.filter(active=True)
    context = {
        'object': object
    }
    
    return render(request, 'home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, active=True)
    context = {
        'product': product,
    }
    print(context)
    return render(request, 'product.html', context)




        