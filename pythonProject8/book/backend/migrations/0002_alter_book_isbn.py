# Generated by Django 5.1.1 on 2024-09-09 11:33

import backend.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(validators=[backend.validators.validate_isbn], verbose_name='ISBN'),
        ),
    ]
