from rest_framework import permissions, viewsets
import django_filters.rest_framework
from .models import Category, Product, CartItem, Filter
from .permissions import IsAuthorOrAdmin, IsAuthor
from .serializers import CategorySerializer, ProductSerializer, CartItemSerializer, ProductFilterSerializer, FilterSerializer
from rest_framework import generics


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthorOrAdmin(),)
        elif self.request.method in ['PUT', 'PATCH']:
            return (IsAuthorOrAdmin(),)
        return (permissions.AllowAny(),)


class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthorOrAdmin(),)
        elif self.request.method in ['PUT', 'PATCH']:
            return (IsAuthor(),)
        return (permissions.AllowAny(),)

class CartListAPIView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthorOrAdmin(),)
        elif self.request.method in ['PUT', 'PATCH']:
            return (IsAuthor(),)
        return (permissions.AllowAny(),)

#
# class ProductFilterListAPIView(viewsets.ModelViewSet):
#     queryset = Product.objects.filter(category_id=1)
#
#     # def get_queryset(self):
#     #     category = self.kwargs['category']
#     #     return Product.objects.filter(product_category=category)
#
#     serializer_class = ProductFilterSerializer

class ProductFilterListAPIView(viewsets.ModelViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset