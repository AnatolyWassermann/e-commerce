from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'size', 'quantity', 'price', 'category', 'active', 'created']
    list_editable = ['price', 'quantity', 'active']
    list_filter = ['active']
    search_fields = ['title', 'size', 'category__title']
    

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

admin.site.register(Category, CategoryAdmin)

