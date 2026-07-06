from django.urls import path
from .views import listarventas, crearventa

urlpatterns = [
    path('', listarventas),
    path('nuevo/', crearventa),
]