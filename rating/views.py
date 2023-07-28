from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rating.models import Rating
from .serializers import RatingSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    @action(detail=True, methods=['POST'])
    def rate_product(self, request, pk=None):
        rating_instance = Rating.objects.all()
        rating_value = request.data.get('rating')
        if not rating_value:
            return Response({'error': 'Rating value is required.'}, status=status.HTTP_400_BAD_REQUEST)

        product = self.get_object()
        user = request.user

        rating, created_at = Rating.objects.update_or_create(
            product=product,
            owner=user,
            rating=rating_instance.оценка
        )

