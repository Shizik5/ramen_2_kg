from rest_framework import serializers
from .models import Comment
from product.models import Product


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        product = self.context.get('product')
        product = Product.objects.get(id=product.id)
        owner = self.context.get('owner')
        validated_data['owner'] = owner
        validated_data['product'] = product
        return super().create(validated_data)