from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import OrderCreateView

router = DefaultRouter()
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/order/', OrderCreateView.as_view()),# name='order-create'),
]