from django.db import models

class Producto(models.Model):
    codigo_barras = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo_barras} - {self.nombre}"