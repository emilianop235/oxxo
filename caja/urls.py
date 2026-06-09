from django.urls import path
from . import views

urlpatterns = [
    path('caja/', views.caja, name='caja'),
]