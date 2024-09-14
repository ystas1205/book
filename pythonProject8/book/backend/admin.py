from django.contrib import admin

from backend.models import Book, User
from setuptools.extern import names


# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year_of_publication', 'ISBN')
    list_display_links = ('id', 'title')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'registration_date')
    list_display_links = ('id',)
