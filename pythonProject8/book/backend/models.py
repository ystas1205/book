from django.utils import timezone

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from backend.validators import validate_isbn
from django.template.defaultfilters import title


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    registration_date = models.DateTimeField(default=timezone.now, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=80, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    year_of_publication = models.DateField(verbose_name='Год издания')
    ISBN = models.CharField(validators=[validate_isbn], verbose_name='ISBN')


    def __str(self):
        return  f"{self.title}"
