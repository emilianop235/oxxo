from django.db import models
from productos.models import Producto
from caja.models import Caja
from clientes.models import Cliente # <-- NUEVA IMPORTACIÓN

class Venta(models.Model):
    caja = models.ForeignKey(Caja, on_delete=models.SET_NULL, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    # NUEVA RELACIÓN: Se conecta con el cliente (opcional por si no tiene tarjeta)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True) 
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"Venta: {self.producto.nombre} x {self.cantidad}"