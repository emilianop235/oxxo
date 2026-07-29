from django.urls import path
from .views import (
    listarventas, 
    listar_todas_ventas, 
    crearventa, 
    desactivarventa, 
    editarventa, 
    consultarventa, 
    listar_inactivos, 
    restaurarventa
)

urlpatterns = [
    path('', listarventas),
    path('todos/', listar_todas_ventas),
    path('nuevo/', crearventa),
    path('desactivar/<int:id>/', desactivarventa),
    path('editar/<int:id>/', editarventa),
    path('consultar/<int:id>/', consultarventa),
    path('inactivos/', listar_inactivos, name='ventas_inactivos'),
    path('restaurar/<int:id>/', restaurarventa, name='restaurar_venta'),
]