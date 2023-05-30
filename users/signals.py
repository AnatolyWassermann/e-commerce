from django.db.models.signals import post_save
from django.dispatch import receiver
from users.tasks import send_mail_notification
from .models import User

@receiver(post_save, sender=User)
def send_new_account_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to my E-Commerce API Project'
        message = 'Thank you for creating an account'
        recipient = [instance.email]
        send_mail_notification.delay(subject, message, recipient)
