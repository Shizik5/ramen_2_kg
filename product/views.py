from rest_framework import permissions, viewsets
import django_filters.rest_framework
from .models import Category, Product, CartItem, Filter
from .permissions import IsAuthorOrAdmin, IsAuthor
from .serializers import CategorySerializer, ProductSerializer, CartItemSerializer, ProductFilterSerializer, FilterSerializer
from rest_framework import generics
from comment.tasks import send_new_comment_email
from rest_framework.decorators import action
from comment.serializers import CommentSerializer
from rest_framework.response import Response


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

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def comments(self, request, pk):
        product = self.get_object()
        user = request.user
        if request.method == 'GET':
            comments = product.comments.all()
            serializer = CommentSerializer(instance=comments, many=True)
            return Response(serializer.data, status=200)

        elif request.method == 'POST':
            serializer = CommentSerializer(data=request.data, context={'product': product, 'owner': user})
            serializer.is_valid(raise_exception=True)
            comment = serializer.save()
            send_new_comment_email.delay(comment.id)
            return Response(serializer.data, status=201)

        elif request.method == 'DELETE':
            comment_id = self.request.query_params.get('id')
            comment = product.comments.filter(product=product, pk=comment_id)

            if comment.exists():
                comment.delete()
                return Response('Successfully deleted', status=204)
        return Response('Not found', status=404)

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