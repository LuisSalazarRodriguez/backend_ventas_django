from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Linea)
admin.site.register(Marca)
admin.site.register(UnidadMedida)
admin.site.register(Moneda)
admin.site.register(Producto)