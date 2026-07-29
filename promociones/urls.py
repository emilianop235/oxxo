from django.urls import path
from .views import *

urlpatterns = [
    path('', listarpromociones),
    path('todos/', listar_todas_promociones),
    path('nuevo/', crearpromocion),
    path('desactivar/<int:id>/', desactivarpromocion),
    path('editar/<int:id>/', editarpromocion),
    path('consultar/<int:id>/', consultarpromocion),
    path('inactivos/', listar_inactivos),
    path('restaurar/<int:id>/', restaurarpromocion),
]