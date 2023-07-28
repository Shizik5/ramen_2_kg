from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from likes.views import LikeCreateView, FavoriteAPIView

router = DefaultRouter()
router.register('likes', LikeCreateView)
router.register('favorites', FavoriteAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
