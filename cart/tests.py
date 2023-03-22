from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product, Category
from .models import Cart, CartItem
import random


class CartModelTestCase(TestCase):
    def setUp(self):
        self.price1 = random.randint(1, 49)
        self.price2 = random.randint(1, 49)
        
        self.user = User.objects.create(
            username='testuser', password='testpassword', email='test@example.com'
        )
        # post save signal already created the cart object for user
        self.cart = Cart.objects.get(user=self.user)
        self.category = Category.objects.create(title='Shirts')
        self.product1 = Product.objects.create(
            title='Product 1', price=self.price1, category=self.category
        )
        self.product2 = Product.objects.create(
            title='Product 2', price=self.price2, category=self.category
        )

    def test_cart_str(self):
        self.assertEqual(str(self.cart), f"{self.user.username}'s cart")

    def test_get_total(self):
        quantityA = random.randint(1, 10)
        quantityB = random.randint(1, 10)
        totalsum = (self.price1 * quantityA) + (self.price2 * quantityB)
        CartItem.objects.create(cart=self.cart, product=self.product1, quantity=quantityA)
        CartItem.objects.create(cart=self.cart, product=self.product2, quantity=quantityB)
        self.assertEqual(self.cart.get_total, totalsum)


class CartItemModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword', email='test@example.com'
        )
        # post save signal already created the cart object for user
        self.cart = Cart.objects.get(user=self.user)
        self.category = Category.objects.create(title='Shirts')
        self.price = random.randint(1, 49)
        self.product = Product.objects.create(
            title='Test Product', price=self.price, category=self.category
        )
        self.quantity = random.randint(1, 10)
        self.cart_item = CartItem.objects.create(
            cart=self.cart, product=self.product, quantity=self.quantity
        )

    def test_cart_item_str(self):
        self.assertEqual(
            str(self.cart_item),
            f"{self.cart.user.username}'s cart item N{self.cart.id} for {self.product.title}",
        )

    def test_get_subtotal(self):
        self.assertEqual(self.cart_item.get_subtotal(), self.product.price * self.quantity)