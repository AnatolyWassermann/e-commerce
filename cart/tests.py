from django.test import TestCase
from django.contrib.auth.models import User
from .models import Cart, CartItem
from products.models import Product, Category
import random

class CartTestCase(TestCase):
    def setUp(self):
        self.rng = random.randint(1, 49)
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')
        category = Category.objects.create(title="Gomlekler")
        self.product1 = Product.objects.create(title='Product 1', price=10, category=category)
        self.product2 = Product.objects.create(title='Product 2', price=20, category=category)
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item1 = CartItem.objects.create(product=self.product1, quantity=self.rng, cart=self.cart)
        self.cart_item2 = CartItem.objects.create(product=self.product2, quantity=self.rng, cart=self.cart)

    def test_cart_item_creation_validation(self):

        self.assertEqual(self.cart_item1.product, self.product1)
        self.assertEqual(self.cart_item1.quantity, self.rng)
        self.assertEqual(self.cart_item1.cart, self.cart)
    
    def test_str_presentation(self):
        self.assertEqual(str(self.cart_item1), f"{self.rng} x {self.product1.title}")
        self.assertEqual(str(self.cart), f"{self.user}'s Cart")



    def test_cart_total_price(self):

        expected_cart_total_price = self.rng * (self.product1.price + self.product2.price)
        expected_cart_item_price = self.rng * self.product1.price
        
        self.assertEqual(self.cart.total_price, expected_cart_total_price)
        self.assertEqual(self.cart_item1.total_price, expected_cart_item_price)