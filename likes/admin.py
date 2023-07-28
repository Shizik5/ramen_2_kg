from django.contrib import admin
from likes.models import Like, Favorites
# Register your models here.
admin.site.register(Like),
admin.site.register(Favorites)