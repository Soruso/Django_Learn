from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import Article
from rest_framework.response import Response
from serializers import ArticleSerializer
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework import viewsets
from rest_framework import mixins
from .filters import ArticleFilters
from rest_framework.pagination import LimitOffsetPagination


def get(request, format=None):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response


class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class ArticleLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleLimitOffsetPagination


class ArticleCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilters


class ArticleDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['name', 'user']


class ArticleCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                           mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class ArticleModelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = ArticleSerializer


class ArticleViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

    @action(detail=True, methods=['get'])
    def article_text_only(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        return Response({'article.txt': article.text})

    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class ArticleAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializers_class = ArticleSerializer


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
