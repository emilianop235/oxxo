from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    estatus = models.BooleanField(default=True) # Campo para papelera lógica

    def __str__(self):
        return f"{self.nombre} {self.apellido}"