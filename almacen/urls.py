from django.urls import path
from . import views

urlpatterns = [
    path('almacen/', views.almacen, name='almacen'),
]