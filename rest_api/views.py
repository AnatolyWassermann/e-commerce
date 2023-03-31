from products.models import Product, Category, ProductFav
from cart.models import Cart, CartItem
from .serializers import (ProductSerializer, CategorySerializer, 
                          ProductFavSerializer, CartItemSerializer,
                          CartSerializer)
from .filters import (ProductFilter, CategoryFilter, 
                      ProductFavFilter, CartItemFilter,
                      CartFilter)
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_cookie
from rest_framework.views import  APIView




class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*15))
    def dispatch(self, *args, **kwargs):
        return super(ProductViewSet, self).dispatch(*args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*15))
    def dispatch(self, *args, **kwargs):
        return super(CategoryViewSet, self).dispatch(*args, **kwargs)
    
class ProductFavViewSet(viewsets.ModelViewSet):

    queryset = ProductFav.objects.all()
    serializer_class = ProductFavSerializer
    filterset_class = ProductFavFilter
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*15))
    def dispatch(self, *args, **kwargs):
        return super(ProductFavViewSet, self).dispatch(*args, **kwargs)
    
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    filterset_class = CartItemFilter

    @action(detail=True)
    def subtotal(self, request, pk=None):
        cart_item = self.get_object()
        subtotal = cart_item.get_subtotal()
        return Response({'subtotal': subtotal})    
    
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*15))
    def dispatch(self, *args, **kwargs):
        return super(CartItemViewSet, self).dispatch(*args, **kwargs)
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filterset_class = CartFilter

    @action(detail=True)
    def total(self, request, pk=None):
        cart = self.get_object()
        total = cart.get_total()
        return Response({'total': total})
    
    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*15))
    def dispatch(self, *args, **kwargs):
        return super(CartViewSet, self).dispatch(*args, **kwargs)


class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class CategoryDetailApiView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

class ProductFavDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductFav.objects.all()
    serializer_class = ProductFavSerializer
    lookup_field = 'pk'

class CartItemDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = 'pk'
  
class CartDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'pk'


