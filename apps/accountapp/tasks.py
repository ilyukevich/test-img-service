from config.celery import app
from django.core.mail import send_mail
from .models import User


@app.task
def user_created(username):

    user = User.objects.get(username=username)
    email = user.email
    subject = 'Account created'
    message = 'Dear user, account created!'
    mail_sent = send_mail(subject, message, 'info@img-service.com', [email])

    return mail_sent
