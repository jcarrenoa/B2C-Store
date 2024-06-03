from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Descuento)
admin.site.register(Evento)
admin.site.register(Carrito)
admin.site.register(DetallesCarrito)
admin.site.register(Mensaje)
admin.site.register(Orden)