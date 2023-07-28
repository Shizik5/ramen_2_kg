from django.db import models

from registration.models import CustomUser
from product.models import Product

RATING_CHOICES = (
    (1, 'очень плохо'),
    (2, 'плохо'),
    (3, 'нормально'),
    (4, 'хорошо'),
    (5, 'очень хорошо')
)

class Rating(models.Model):
    product = models.ForeignKey(Product, related_name='rating', on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, related_name='rating', on_delete=models.CASCADE)
    оценка = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} - {self.product} - оценка: {self.оценка}'

    class Meta:
        unique_together = ['owner', 'product', 'оценка']
