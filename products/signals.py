from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product
from django.utils.text import slugify
import random 


@receiver(pre_save, sender=Product)
def autoslug(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        print(f"{instance.slug} slug created for {instance.title}")
    if not instance.size:
        instance.size = random.choices(Product.SIZE_CHOICES)[0][0]       
        print(f"Size for {instance.title} is {instance.size}")


