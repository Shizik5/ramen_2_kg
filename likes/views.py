from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter

from .models import Like
from .serializers import LikeSerializer, RecomendSerializer
from product.permissions import IsAuthor
from rest_framework.pagination import PageNumberPagination

from rest_framework.viewsets import ModelViewSet
# Create your views here.


class StandartResultPagination (PageNumberPagination):
    page_size = 5
    page_query_param = 'page'


class LikeCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAuthor)
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LileDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAuthor)
    lookup_field = 'id'

# class RecomendView(generics.CreateAPIView):
#     queryset = Recomend.objects.all()
#     permissions_classes = (permissions.IsAuthenticated)
#     serializer_class = RecomendSerializer
#     pagination_class = StandartResultPagination
#     filter_backends = (SearchFilter, DjangoFilterBackend)
#     search_filter = ('title',)
#     filterset_fields = ('title')
#
#     def get_recomends(self):
#         if self.action == 'recomends':
#             return RecomendSerializer
#         return FavoriteSerializer
