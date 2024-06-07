# Generated by Django 5.0.6 on 2024-06-04 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Имя')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='avatars/%Y/%m/%d/', verbose_name='Фото')),
                ('salary', models.PositiveIntegerField(verbose_name='Оклад')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Список сотрудников',
            },
        ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('employee', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Департамент',
                'verbose_name_plural': 'Список департаментов',
            },
        ),
    ]
