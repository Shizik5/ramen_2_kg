from rest_framework import serializers
from .models import Like, Favorite

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    user_username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Like
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        product = attrs['product']
        if user.likes.filter(product=product).exists():
            raise serializers.ValidationError(
                'you have already liked this product!'
            )
        return attrs

class LikedUserSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    user_username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Like
        fields = ['user', 'user_username']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'product')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product_title'] = instance.product.title
        if instance.product.preview:
            preview = instance.product.preview
            representation['product_preview'] = preview.url
        else:
            representation['product_preview'] = None
        return representation

# class RecomendSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recomend
#         fields = ('id', 'product')
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['product_title'] = instance.product.title
#         if instance.product.preview:
#             preview = instance.product.preview
#             representation['product_preview'] = preview.url
#         else:
#             representation['product_preview'] = None
#         return representation