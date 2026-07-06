from django.urls import path
from .views import listaralmacen, crearalmacen

urlpatterns = [
    path('', listaralmacen),
    path('nuevo/', crearalmacen),
]
