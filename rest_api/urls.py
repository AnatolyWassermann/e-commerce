from django.urls import path, include
from .views import (ProductViewSet, CategoryViewSet,
                    ProductDetailApiView, CategoryDetailApiView,
                    ProductFavViewSet, ProductFavDetailApiView,
                    CartItemViewSet, CartItemDetailApiView,
                    CartViewSet, CartDetailApiView)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'productfavs', ProductFavViewSet)
router.register(r'cartitems', CartItemViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = [
path('', include(router.urls)),
path('product/<int:pk>/', ProductDetailApiView.as_view(), name='product_detail'),
path('category/<int:pk>/', CategoryDetailApiView.as_view(), name='category_detail'),
path('productfav/<int:pk>/', ProductFavDetailApiView.as_view(), name='productfav_detail'),
path('cartitem/<int:pk>/', CartItemDetailApiView.as_view(), name='cartitem_detail'),
path('cart/<int:pk>/', CartDetailApiView.as_view(), name='cart_detail')
]