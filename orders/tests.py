from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order, OrderItem
from products.models import Product, Category
import random


class OrderModelTestCase(TestCase):
    def setUp(self):
        self.rng1 = random.randint(1, 49)
        self.rng2 = random.randint(1, 49)
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')
        self.order = Order.objects.create(user=self.user)
        category = Category.objects.create(title="Gomlekler")
        self.product1 = Product.objects.create(title='Test Product 1', price=10.0, category=category)
        self.product2 = Product.objects.create(title='Test Product 2', price=20.0, category=category)
        self.orderitem1 = OrderItem.objects.create(order=self.order, product=self.product1, quantity=self.rng1)
        self.orderitem2 = OrderItem.objects.create(order=self.order, product=self.product2, quantity=self.rng2)

    def test_str_presentation(self):

        self.assertEqual(str(self.order), f"{self.user}'s Order")

    def test_order_total_price(self):
        
        expected_order_total_price =  (self.rng1 * self.product1.price) + (self.rng2 * self.product2.price) 

        self.assertEqual(self.order.total_price, expected_order_total_price)


class OrderItemModelTestCase(TestCase):
    def setUp(self):
        self.rng = random.randint(1, 49)
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')
        self.order = Order.objects.create(user=self.user)
        category = Category.objects.create(title="Gomlekler")
        self.product = Product.objects.create(title='Test Product 1', price=10.0, category=category)
        self.order_item = OrderItem.objects.create(
            order=self.order, product=self.product, quantity=self.rng)

    def test_str_presentation(self):
        expected = f"{self.rng}x {self.product} in {self.order}"
        self.assertEqual(str(self.order_item), expected)

    def test_order_item_total_price(self):
        expected_order_item_price = self.rng * self.product.price
        self.assertEqual(self.order_item.total_price, expected_order_item_price)