from django.db import models

class caja(models.Model):
    numero = models.CharField(max_length=20)
    usuario = models.Aggregated('empleado__nombre', distinct=True)
    turno = models.Aggregated('turno__nombre', distinct=True)
    