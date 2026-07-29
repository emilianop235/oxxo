from django.db import models
from productos.models import Producto

class almacen(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

# Esto representa la tienda física
class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Esto representa cuántos productos hay en la tienda
class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    ubicacion = models.CharField(max_length=100, default='Piso de venta')
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad} Unds en {self.sucursal.nombre}"