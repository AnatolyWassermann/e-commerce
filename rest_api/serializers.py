from products.models import Product, Category, ProductFav
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "product_detail",
        lookup_field = "pk")
    class Meta:
        model = Product
        fields = ['url', 'id', 'title', 'slug', 'size', 'price', 'desc', 
                  'image_url', 'quantity', 'active', 'created']
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "category_detail",
        lookup_field = "pk")
   
    class Meta:
        model = Category
        fields = ['url', 'id', 'title']