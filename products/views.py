from django.shortcuts import render
from .models import Product, Category
import requests
import random
from django.http import HttpResponse



def populate_db(request):
    r = requests.get('https://fakestoreapi.com/products')
    for item in r.json():
        category_title = item['category']
        Category.objects.get_or_create(title=category_title)
        product = Product(
            title = item['title'],
            desc = item['description'],
            price = item['price'],
            image_url = item['image'],
            quantity = random.randint(1, 49),
            active = True,
            category = Category.objects.get(title=category_title)
        )
        product.save()

    return HttpResponse('<p>Database populated!</p>')

