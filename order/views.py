from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer
from .tasks import send_confirmation_email
from rest_framework import status
from django.core.cache import cache
from rest_framework.generics import CreateAPIView


# Create your views here.

class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()  # Replace 'Order' with the name of your model
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        # cart_items = CartItem.objects.filter(user=user, ordered=True)

        if cart_items:
            total_price = sum(item.quantity * item.product.price for item in cart_items)
            order = Order.objects.create(user=user, total_price=total_price)
            order.items.set(cart_items)
            cart_items.delete()
            send_confirmation_email.delay(order.id, user.email)
            cache.delete(f'user_{user.id}_order')

            return Response({"message": "Заказ успешно оформлен."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Нет товаров в корзине для оформления заказа."},
                            status=status.HTTP_400_BAD_REQUEST)