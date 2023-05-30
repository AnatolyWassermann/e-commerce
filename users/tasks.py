from django.core.mail import send_mail
from ecommerce.celery import app

@app.task
def send_mail_notification(recipient, subject, message):
    send_mail(subject, message, 'seruderu@gmail.com', [recipient])