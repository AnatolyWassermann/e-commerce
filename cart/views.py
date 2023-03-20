from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product


@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    product = cart_item.product
    cart.products.add(product)
    cart.save()
    return redirect('product', slug)

@login_required
def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
     # calculate total cart price using @property
    total = cart.get_total
    if request.method == 'POST':
        for item in cart.items.all():
            quantity = request.POST.get(f'quantity_{item.id}')
            if quantity is not None:
                try:
                    if int(quantity) < 1:
                        quantity = 1
                    if int(quantity) > item.product.quantity:
                        quantity = item.product.quantity
                except ValueError:
                    quantity = 1
                item.quantity = int(quantity)
                item.save()
        # if cart is updated calculate total again
        total = cart.get_total
    context = {
        'cart': cart,
        'total': total
    }

    return render(request, 'cart_detail.html', context)

@login_required
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = Cart.objects.get(user=request.user)
    cart.products.remove(product)
    return redirect('cart:cart_detail')

