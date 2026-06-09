from django.shortcuts import render
from django.http import HttpResponse

def almacen(request):
    return render(request, 'almacen/almacen.html')