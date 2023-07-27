from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import *

router = DefaultRouter()
router.register('cart', CartListAPIView)
router.register('product', ProductAPIView)
router.register('category', CategoryAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('filter/', ProductFilterListAPIView.as_view()),
]
