from django.urls import path
from .views import home_page, product_page

urlpatterns = [
    path('', home_page, name='home'),
    path('product/<slug:slug>/', product_page, name='product')
   
]
