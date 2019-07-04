from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from book.models import Book, Category
from .serializer import BookSerializer,CategorySerializer

class BookApiViewAll(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'


class CategoryApiViewAll(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class BookApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'


class CategoryApiView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

