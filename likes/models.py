from django.db import models
from product.models import Product
from registration.models import CustomUser
from project import settings
# Create your models here.
class Like(models.Model):
    product = models.ForeignKey(Product, related_name='likes', on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, related_name='likes', on_delete=models.CASCADE)


class Favorites(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='favorites', on_delete=models.CASCADE)
    post = models.ForeignKey(Product, related_name='favorites', on_delete=models.CASCADE)

# class Recomend(models.Model):
#     user = models.ForeignKey('User', related_name='recomend', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, related_name='recomend', on_delete=models.CASCADE)