from django.urls import path
from backend.views import BookView, RegisterUser
from backend import views

app_name = 'backend'
urlpatterns = [
    path('book', BookView.as_view(), name='book'),
    path('book/<int:pk>/', BookView.as_view(), name='book_id'),
    path('registeruser', RegisterUser.as_view(), name='registeruser'),
    path('books/add_book/', views.add_book, name='add_book'),

]
