from django_filters import rest_framework as filters
from products.models import Product

class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    price = filters.NumberFilter(lookup_expr='icontains')
    quantity = filters.NumberFilter(lookup_expr='icontains')
    active = filters.BooleanFilter(lookup_expr='icontains')
    created = filters.DateFilter()
    size = filters.ChoiceFilter(choices=Product.SIZE_CHOICES)

    class Meta:
        model = Product
        fields = ['title', 'price', 'quantity', 'active', 'size', 'created']

