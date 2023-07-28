from rest_framework import serializers
from .models import Category, Product, CartItem, Filter
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = ('id', 'category', 'title')

class ProductFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'image')

class FilterSerializer(serializers.ModelSerializer):
    title = ProductFilterSerializer(many=False, read_only=True)  # Определяем сериализатор для связанной модели Product

    class Meta:
        model = Filter
        fields = ('id', 'category', 'title')