from django.urls import path
from .views import (
    listarproductos, 
    listar_todos_productos, 
    crearproducto, 
    desactivarproducto, 
    editarproducto, 
    consultarproducto, 
    listar_inactivos, 
    restaurarproducto
)

urlpatterns = [
    path('', listarproductos),
    path('todos/', listar_todos_productos),
    path('nuevo/', crearproducto),
    path('desactivar/<int:id>/', desactivarproducto),
    path('editar/<int:id>/', editarproducto),
    path('consultar/<int:id>/', consultarproducto),
    path('inactivos/', listar_inactivos, name='productos_inactivos'),
    path('restaurar/<int:id>/', restaurarproducto, name='restaurar_producto'),
]