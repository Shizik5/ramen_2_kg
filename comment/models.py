from django.db import models
from product.models import Product
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE, related_query_name='products')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} commented {self.product}: {self.body}'


