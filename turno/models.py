from django.db import models

class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre