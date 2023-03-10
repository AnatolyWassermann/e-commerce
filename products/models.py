from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']

    def __str__(self):
        return self.title



class Product(models.Model):

    EXTRA_SMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'

    SIZE_CHOICES = [
        (EXTRA_SMALL, 'XS'),
        (SMALL, 'S'),
        (MEDIUM, 'M'),
        (LARGE, 'L'),
        (EXTRA_LARGE, 'XL')
    ]



    title = models.CharField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.TextField(null=True, blank=True)
    image = models.CharField(null=True, blank=True, max_length=200)
    quantity = models.PositiveBigIntegerField(default=0)
    active = models.BooleanField(default=False)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='products', null=True, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES, default=MEDIUM)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title



