from django.urls import path, include
from .views import (ProductViewSet, CategoryViewSet,
                    ProductDetailApiView, CategoryDetailApiView,
                    ProductFavViewSet, ProductFavDetailApiView,
                    CartItemViewSet, CartItemDetailApiView,
                    CartViewSet, CartDetailApiView,)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'productfavs', ProductFavViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = [
path('', include(router.urls)),
path('product/<int:pk>/', ProductDetailApiView.as_view(), name='product_detail'),
path('category/<int:pk>/', CategoryDetailApiView.as_view(), name='category_detail'),
path('productfav/<int:pk>/', ProductFavDetailApiView.as_view(), name='productfav_detail'),
path('cart-item/<int:pk>/', CartItemDetailApiView.as_view(), name='cartitem_detail'),
path('cart-item/<int:pk>/subtotal/', CartItemViewSet.as_view({'get': 'subtotal'}), name='cart-item-subtotal'),
path('cart/<int:pk>/', CartDetailApiView.as_view(), name='cart_detail'),
path('cart/<int:pk>/subtotal/', CartViewSet.as_view({'get': 'total'}), name='cart-total')
]