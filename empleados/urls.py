from django.urls import path
from .views import (
    listarempleados, 
    listar_todos_empleados, 
    crearempleado, 
    desactivarempleado, 
    editarempleado, 
    consultarempleado, 
    listar_inactivos, 
    restaurarempleado
)

urlpatterns = [
    path('', listarempleados),
    path('todos/', listar_todos_empleados),
    path('nuevo/', crearempleado),
    path('desactivar/<int:id>/', desactivarempleado),
    path('editar/<int:id>/', editarempleado),
    path('consultar/<int:id>/', consultarempleado),
    path('inactivos/', listar_inactivos, name='empleados_inactivos'),
    path('restaurar/<int:id>/', restaurarempleado, name='restaurar_empleado'),
]