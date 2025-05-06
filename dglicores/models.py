from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.identificacion} - {self.nombre}"
    
class Licor(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)  
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    contenido_alcoholico = models.DecimalField(max_digits=5, decimal_places=2)  

    def __str__(self):
        return f"{self.nombre} - {self.marca}"
    
class Inventario(models.Model):
    licor = models.ForeignKey(Licor, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.licor.nombre}: {self.cantidad} unidades"

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    licor = models.ForeignKey(Licor, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta a {self.cliente.nombre} - {self.licor.nombre} x{self.cantidad}"