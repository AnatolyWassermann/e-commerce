from django.db import models
from products.models import Product
from users.models import User


    
class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE, unique=True)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"{self.user.email}'s cart"
    
    def get_total(self):
        cart_items = CartItem.objects.filter(cart=self)
        total = sum(item.get_subtotal() for item in cart_items)
        return total
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name= 'items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cart.user.email}'s cart item N{self.id} for {self.product.title}"

    def get_subtotal(self):
        return self.product.price * self.quantity
    
