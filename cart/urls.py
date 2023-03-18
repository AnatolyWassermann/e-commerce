from django.urls import path
from .views import add_to_cart, cart_detail, remove_from_cart

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('remove/<slug:slug>/', remove_from_cart, name='remove_from_cart'),
   
]
