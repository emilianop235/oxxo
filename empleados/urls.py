from django.urls import path
from .views import listarempleados, crearempleado

urlpatterns = [
    path('', listarempleados),          # <-- Esto debe estar completamente vacío ''
    path('nuevo/', crearempleado),      # Procesa el formulario
]