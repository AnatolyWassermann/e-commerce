from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.TextField()
    image = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title



