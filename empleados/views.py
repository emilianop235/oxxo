from django.shortcuts import render, redirect
from .models import Empleado

def listarempleados(request):
    # Solicitamos a PostgreSQL la lista completa de empleados
    consultaempleados = Empleado.objects.all()
    return render(request, 'empleado/empleado.html', {'consultaempleados': consultaempleados})

def crearempleado(request):
    if request.method == 'POST':
        Empleado.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            correo=request.POST['correo'],
            telefono=request.POST['telefono']
        )
    return redirect('/pageempleados/')