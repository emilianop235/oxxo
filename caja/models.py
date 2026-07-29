from django.db import models
from empleados.models import Empleado
from turno.models import Turno
from almacen.models import Sucursal # Importamos la sucursal para ubicar la caja

class Caja(models.Model):
    numero = models.CharField(max_length=20)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='cajas')
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name='cajas')
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"Caja {self.numero} - {self.sucursal.nombre if self.sucursal else 'Sin Sucursal'}"