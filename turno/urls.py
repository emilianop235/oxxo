from django.urls import path
from .views import (
    listarturnos, 
    listar_todos_turnos, 
    crearturno, 
    desactivarturno, 
    editarturno, 
    consultarturno, 
    listar_inactivos, 
    restaurarturno
)

urlpatterns = [
    path('', listarturnos),
    path('todos/', listar_todos_turnos),
    path('nuevo/', crearturno),
    path('desactivar/<int:id>/', desactivarturno),
    path('editar/<int:id>/', editarturno),
    path('consultar/<int:id>/', consultarturno),
    path('inactivos/', listar_inactivos, name='turnos_inactivos'),
    path('restaurar/<int:id>/', restaurarturno, name='restaurar_turno'),
]