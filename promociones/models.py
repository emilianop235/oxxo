from django.db import models
from productos.models import Producto # <-- RELACIÓN 1

class Promocion(models.Model):
    nombre_promo = models.CharField(max_length=100, help_text="Ej. Promo 2x1 Coca-Cola")
    # Relación: ¿A qué producto se le aplica este descuento?
    producto_en_promocion = models.ForeignKey(Producto, on_delete=models.CASCADE)
    porcentaje_descuento = models.IntegerField(help_text="Ej. 10 para 10% de descuento")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_promo} ({self.porcentaje_descuento}%)"