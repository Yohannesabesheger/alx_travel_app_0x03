from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(email, name, booking_id):
    subject = 'Booking Confirmation'
    message = f"Hello {name},\n\nYour booking with ID {booking_id} has been confirmed. Thank you!"
    from_email = None  # use DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
