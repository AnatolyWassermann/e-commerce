from django.urls import path, include
from .views import ProductViewSet, CategoryViewSet, ProductDetailApiView, CategoryDetailApiView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
path('', include(router.urls)),
path('product/<int:pk>/', ProductDetailApiView.as_view(), name='product_detail'),
path('category/<int:pk>/', CategoryDetailApiView.as_view(), name='category_detail')
]