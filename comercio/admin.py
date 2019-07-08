from django.contrib import admin
from .models import Productor, Producto, Post, Solicitud, Pedido
# Register your models here.

admin.site.register(Post)
admin.site.register(Producto)
admin.site.register(Productor)
admin.site.register(Solicitud)
admin.site.register(Pedido)
