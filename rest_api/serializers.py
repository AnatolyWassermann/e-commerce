from products.models import Product, Category, ProductFav
from rest_framework import serializers
from django.contrib.auth.models import User


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "product_detail",
        lookup_field = "pk")
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    
    class Meta:
        model = Product
        fields = ['url', 'id', 'title', 'slug', 'size', 'price', 'desc', 
                  'category', 'image_url', 'quantity', 'active', 'created']
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "category_detail",
        lookup_field = "pk")
   
    class Meta:
        model = Category
        fields = ['url', 'id', 'title']

class ProductFavSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "productfav_detail",
        lookup_field = "pk")
    user =  serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = ProductFav
        fields = ['url', 'id', 'user', 'product']
    