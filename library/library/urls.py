from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.authors.models import Author
from mainapp import views

router = DefaultRouter()
router.registry('authors', Author)
router.registry('base', views.ArticleViewSet, basename='article')

urlpatterns = [
    path('views/api-view/', views.ArticleAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('viewsets/', include(router.urls)),
]
