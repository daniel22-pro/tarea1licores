from django.contrib import admin
from .models import Venta,Inventario,Licor,Cliente

# Register your models here.
admin.site.register(Venta)
admin.site.register(Inventario)
admin.site.register(Licor)
admin.site.register(Cliente)

