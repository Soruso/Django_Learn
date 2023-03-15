from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorSerializer, BiographySerializer, ArticleSerializer, BookSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class AuthorViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BiographyViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = BiographySerializer


class BookViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = BookSerializer


class ArticleViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = ArticleSerializer
