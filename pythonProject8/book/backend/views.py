from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.serializers import BookSerializer, UserSerializer

from backend.models import Book


# Create your views here.


class BookView(APIView):

    def post(self, request, *args, **kwargs):

        if {'title', 'author', 'year_of_publication',
            'ISBN'}.issubset(request.data):
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return JsonResponse({'status': 'Книга добавлена'},
                                    status=status.HTTP_201_CREATED)
        return JsonResponse(
            {'Status': 'Не указаны все необходимые аргументы'},
            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, *args, **kwargs):
        if pk is None:
            books = Book.objects.all()

            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            try:
                cargos = Book.objects.get(id=pk)
            except Book.DoesNotExist:
                return JsonResponse({'error': 'Данной книги нет'},
                                    status=404)
            serializer = BookSerializer(cargos)
            return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """ Удаление книги по ID """
        items_sting = request.data.get('items')
        if items_sting:
            items_list = items_sting.split(',')
            query = Q()
            objects_deleted = False
            for book_id in items_list:
                if book_id.isdigit():
                    query = query | Q(id=book_id)
                    objects_deleted = True
                else:
                    return JsonResponse(
                        {'message': 'Введены некорректные данные'},
                        status=status.HTTP_403_FORBIDDEN)
            if objects_deleted:
                deleted_count = Book.objects.filter(query).delete()[
                    0]
                return JsonResponse(
                    {'message': f'Удалено {deleted_count}'},
                    status=status.HTTP_204_NO_CONTENT)
        return JsonResponse(
            {'Status': 'Не указаны все необходимые аргументы'},
            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        if 'id' in request.data:
            if request.data['id'].isdigit():
                try:
                    book = Book.objects.get(id=request.data['id'])
                except Book.DoesNotExist:
                    return Response({'error': 'Данной книги в базе нет'})
                if book:
                    serializer = BookSerializer(book,
                                                data=request.data,
                                                partial=True)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        return Response(
                            {'status': 'Книга обновлена'},
                            status=status.HTTP_201_CREATED)
        return Response(
            {'Status': 'Не указаны все необходимые аргументы'},
            status=status.HTTP_400_BAD_REQUEST)


def add_book(request):
    return render(request, 'books/add_book.html')


class RegisterUser(APIView):

    def post(self, request, *args, **kwargs):
        if {'name', 'email'}.issubset(request.data):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return JsonResponse({'status': 'Регистрация прошла успешно'},
                                    status=status.HTTP_201_CREATED)
        return JsonResponse(
            {'Status': 'Не указаны все необходимые аргументы'},
            status=status.HTTP_400_BAD_REQUEST)
