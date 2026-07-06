from django.shortcuts import render, redirect
from .models import almacen # Importamos el modelo que acabamos de definir arriba

def listaralmacen(request):
    consultaalmacen = almacen.objects.all()
    return render(request, 'almacen/almacen.html', {'consultaalmacen': consultaalmacen})


def crearalmacen(request):
    if request.method == 'POST':
        almacen.objects.create(
            nombre=request.POST['nombre'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono']
        )
    return redirect('/pagealmacen/')