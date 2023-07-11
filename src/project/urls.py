from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='projects')
router.register(r'textures', views.TextureViewSet, basename='textures')


urlpatterns = [
    path('', include(router.urls)),
]
