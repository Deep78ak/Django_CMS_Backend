from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, LikeViewSet
from .gen_token import GenerateTokenViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'get-auth-token', GenerateTokenViewSet, basename='get-auth-token')


urlpatterns = [
    path('', include(router.urls)),
]
