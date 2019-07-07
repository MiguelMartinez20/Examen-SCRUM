from django.contrib import admin
from .models import Productor, Producto, Post
# Register your models here.

admin.site.register(Post)
admin.site.register(Producto)
admin.site.register(Productor)

