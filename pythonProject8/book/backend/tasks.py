from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@shared_task(bind=True)
def task_new_user(self, user_id, email):
    """
    Отправляем письмо с подтрердждением почты
    """

    msg = EmailMultiAlternatives(
        # title:
        f"Регистрация {email}",
        # message:
        'Регистрация прошла успешно',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [email]
    )
    msg.send()
    return 'Done'
