from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_confirmation_email(order_id, recipient_email):
    subject = 'Подтверждение заказа'
    message = f'Спасибо за ваш заказ. Номер заказа: {order_id}'
    from_email = 'darinaibrag@gmail.com'  # Укажите свой email
    recipient_list = [recipient_email]

    send_mail(subject, message, from_email, recipient_list)