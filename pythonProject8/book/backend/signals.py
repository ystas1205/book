from typing import Type
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from backend.tasks import task_new_user
from backend.models import User


@receiver(post_save, sender=User)
def new_user_registered_signal(sender: Type[User], instance: User,
                               created: bool, **kwargs):
    """  Отправляем письмо на почту """
    if created:
        task_new_user.delay(instance.pk,instance.email)

