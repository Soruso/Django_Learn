from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, BookSerializerBase


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BookSerializer
        return BookSerializerBase
