from products.models import Product, Category, ProductFav
from .serializers import ProductSerializer, CategorySerializer, ProductFavSerializer
from rest_framework import viewsets, generics
from .filters import ProductFilter, CategoryFilter, ProductFavFilter
from django_filters import rest_framework as filters
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_cookie



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


