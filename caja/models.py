from django.db import models
from empleados.models import empleado
from turno.models import turno

class caja(models.Model):
    numero = models.CharField(max_length=20)
    usuario = models.ForeignKey(empleado, on_delete=models.CASCADE, related_name='cajas')
    turno = models.ForeignKey(turno, on_delete=models.CASCADE, related_name='cajas')

    def __str__(self):
        return f"Caja {self.numero} - {self.usuario.nombre} - {self.turno.nombre}"
    