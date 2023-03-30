from django_filters import rest_framework as filters
from products.models import Product, Category, ProductFav
from django_filters.widgets import BooleanWidget


class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    price = filters.RangeFilter(field_name='price')
    quantity = filters.RangeFilter(field_name='quantity')
    active = filters.BooleanFilter(widget=BooleanWidget())
    created = filters.DateFromToRangeFilter(
        label='Created Between',
        label_suffix = ' (YYYY-MM-DD)',
        help_text='Filter products created within a date range'
    )
    size = filters.ChoiceFilter(choices=Product.SIZE_CHOICES)

    class Meta:
        model = Product
        fields = ['title', 'price', 'quantity', 'active', 'size', 'created']



class CategoryFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['title']

class ProductFavFilter(filters.FilterSet):
    user = filters.NumberFilter(lookup_expr='exact')
    product = filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = ProductFav
        fields = ['user', 'product']
