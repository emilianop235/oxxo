from django.urls import path
from . import views

urlpatterns = [
    path('turno/', views.turno, name='turno'),
]