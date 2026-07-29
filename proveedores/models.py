from django.db import models
from almacen.models import Sucursal # <-- RELACIÓN 1

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    # Relación: ¿A qué sucursal surte principalmente este proveedor?
    sucursal_base = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True, blank=True)
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return self.empresa