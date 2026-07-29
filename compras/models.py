from django.db import models
from proveedores.models import Proveedor # <-- RELACIÓN 1
from productos.models import Producto    # <-- RELACIÓN 2
from empleados.models import Empleado    # <-- RELACIÓN 3

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    recibido_por = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    cantidad_comprada = models.IntegerField(default=1)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"Compra {self.cantidad_comprada} de {self.producto.nombre}"