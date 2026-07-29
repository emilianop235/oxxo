from django.urls import path
from .views import *

urlpatterns = [
    path('', listarcompras),
    path('todos/', listar_todas_compras),
    path('nuevo/', crearcompra),
    path('desactivar/<int:id>/', desactivarcompra),
    path('editar/<int:id>/', editarcompra),
    path('consultar/<int:id>/', consultarcompra),
    path('inactivos/', listar_inactivos),
    path('restaurar/<int:id>/', restaurarcompra),
]