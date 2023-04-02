from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from library.authors.models import Author
from mainapp import views
from userapp.views import UserListAPIView


router = DefaultRouter()
router.registry('authors', Author)
router.registry('base', views.ArticleViewSet, basename='article')

urlpatterns = [
    path('views/api-view/', views.ArticleAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('viewsets/', include(router.urls)),
    re_path(r'^api/(?P<version>\d\.\d)/users/$', UserListAPIView.as_view()),
    path('api/users/0.1', include('userapp.urls', namespace='0.1')),
    path('api/users/0.2', include('userapp.urls', namespace='0.2')),
]
