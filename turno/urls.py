from django.urls import path
from .views import listarturnos, crearturno

urlpatterns = [
    path('', listarturnos),
    path('nuevo/', crearturno),
]