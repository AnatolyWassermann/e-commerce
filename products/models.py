from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']

    def __str__(self):
        return self.title

class ProductFav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')


class Product(models.Model):

    A = 'XS'
    B = 'S'
    C = 'M'
    D = 'L'
    E = 'XL'

    SIZE_CHOICES = [
        (A, 'XS'),
        (B, 'S'),
        (C, 'M'),
        (D, 'L'),
        (E, 'XL')
    ]

    title = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.TextField(blank=True)
    image_url = models.CharField(null=True, blank=True, max_length=255)
    quantity = models.PositiveBigIntegerField(default=0)
    active = models.BooleanField(default=False)
    favorites = models.ManyToManyField(User, through=ProductFav, related_name='fav_products', blank=True)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, related_name='products', null=True, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    





