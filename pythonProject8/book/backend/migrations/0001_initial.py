# Generated by Django 5.1.1 on 2024-09-09 09:38

import backend.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Название')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('year_of_publication', models.DateField(verbose_name='Год издания')),
                ('ISBN', models.IntegerField(validators=[backend.validators.validate_isbn], verbose_name='ISBN')),
            ],
        ),
    ]
