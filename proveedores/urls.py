from django.urls import path
from .views import *

urlpatterns = [
    path('', listarproveedores),
    path('todos/', listar_todos_proveedores),
    path('nuevo/', crearproveedor),
    path('desactivar/<int:id>/', desactivarproveedor),
    path('editar/<int:id>/', editarproveedor),
    path('consultar/<int:id>/', consultarproveedor),
    path('inactivos/', listar_inactivos),
    path('restaurar/<int:id>/', restaurarproveedor),
]