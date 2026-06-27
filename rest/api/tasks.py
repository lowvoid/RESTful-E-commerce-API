from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_order_confirmation_email(user_email, order_id):
    subject = 'Order Confirmation'
    message = f'Thank you for your order! Your order ID is {order_id}.'
    return send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])
