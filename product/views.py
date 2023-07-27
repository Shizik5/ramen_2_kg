from rest_framework import permissions, viewsets
from .models import Category, Product, CartItem
from .permissions import IsAuthorOrAdmin, IsAuthor
from .serializers import CategorySerializer, ProductSerializer, CartItemSerializer
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


class ProductFilterListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(product__category=category)