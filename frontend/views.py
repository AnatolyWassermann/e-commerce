from django.shortcuts import render, get_object_or_404
from products.models import Product, ProductFav
from django.views.decorators.cache import cache_page


def home_page(request):

    object = Product.objects.filter(active=True)
    if request.method == 'POST' and 'like' in request.POST:
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, pk=product_id, active=True)
        user = request.user
        # check if user has already liked the product
        if user.is_authenticated and not ProductFav.objects.filter(user=user, product=product).exists():
            # if not, create a new like object
            ProductFav.objects.create(user=user, product=product)
    context = {
        'object': object
    }
    return render(request, 'home.html', context)


@cache_page(60*15)
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, active=True)
    context = {
        'product': product,
    }
    return render(request, 'product.html', context)




        