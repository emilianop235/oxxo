from django.urls import path
from .views import (
    listarcajas, 
    listar_todas_cajas, 
    crearcaja, 
    desactivarcaja, 
    editarcaja, 
    consultarcaja, 
    listar_inactivos, 
    restaurarcaja
)

urlpatterns = [
    path('', listarcajas),
    path('todos/', listar_todas_cajas),
    path('nuevo/', crearcaja),
    path('desactivar/<int:id>/', desactivarcaja),
    path('editar/<int:id>/', editarcaja),
    path('consultar/<int:id>/', consultarcaja),
    path('inactivos/', listar_inactivos, name='cajas_inactivos'),
    path('restaurar/<int:id>/', restaurarcaja, name='restaurar_caja'),
]