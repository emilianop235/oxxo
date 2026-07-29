from django.db import models
from almacen.models import Sucursal # <-- RELACIÓN 1

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, unique=True)
    puntos_acumulados = models.IntegerField(default=0)
    # Relación: ¿En qué tienda tramitó su tarjeta Oxxo Premia?
    tienda_registro = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True, blank=True)
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - Puntos: {self.puntos_acumulados}"