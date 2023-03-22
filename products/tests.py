from django.test import TestCase
from .models import Product, Category
from django.utils.text import slugify


class CategoryModelTest(TestCase):
    
    def test_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), 'Categories')

    def test_str_presentation(self):
        category = Category(title="Game Consoles")
        self.assertEqual(str(category), category.title)

class ProductModelTest(TestCase):

    def setUp(self):
        category = Category.objects.create(title="Gomlekler")
        Product.objects.create(title="Beyaz Gomlek", price=99, category=category)

    def test_queryset_exists(self):
        qs = Product.objects.all()
        self.assertTrue(qs.exists())

    def test_str_presentation(self):
        product = Product.objects.all().first()
        self.assertEqual(str(product), product.title)

    def test_slugified_title(self):
        obj = Product.objects.all().first()
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug, slugified_title)





