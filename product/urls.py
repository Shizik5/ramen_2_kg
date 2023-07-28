from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import CartListAPIView, ProductFilterListAPIView, CategoryAPIView, ProductAPIView

router = DefaultRouter()
router.register('cart', CartListAPIView)
router.register('product', ProductAPIView)
router.register('category', CategoryAPIView)
router.register('filter', ProductFilterListAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('filter/', ProductFilterListAPIView.as_view({'get': 'list'})),
]
