from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'size', 'quantity', 'price', 'category', 'active', 'created']
    search_fields = ['title', 'size', 'category__title', 'active']

admin.site.register(Product, ProductAdmin)

admin.site.register(Category)

