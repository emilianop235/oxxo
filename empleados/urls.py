from django.urls import path
from .views import listarempleados, crearempleado

urlpatterns = [
    path('', listarempleados),
    path('nuevo/', crearempleado),
]