from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.authors import AuthorModelViewSet

router = DefaultRouter()
router.registry('authors', AuthorModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
