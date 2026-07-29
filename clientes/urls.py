from django.urls import path
from .views import *

urlpatterns = [
    path('', listarclientes),
    path('todos/', listar_todos_clientes),
    path('nuevo/', crearcliente),
    path('desactivar/<int:id>/', desactivarcliente),
    path('editar/<int:id>/', editarcliente),
    path('consultar/<int:id>/', consultarcliente),
    path('inactivos/', listar_inactivos),
    path('restaurar/<int:id>/', restaurarcliente),
]