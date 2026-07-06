from django.urls import path
from .views import listarcajas, crearcaja

urlpatterns = [
    path('', listarcajas),
    path('nuevo/', crearcaja),
]