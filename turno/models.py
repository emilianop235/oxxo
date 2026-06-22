from django.db import models

class turno(models.Model):
    nombre = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()