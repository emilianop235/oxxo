from django.db import models

class ventas(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)