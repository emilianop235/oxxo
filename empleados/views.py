from django.shortcuts import render, redirect
from .models import empleado

def listarempleados(request):
    # Solicitamos a PostgreSQL la lista completa de empleados
    consultaempleados = empleado.objects.all()
    return render(request, 'empleados/empleados.html', {'consultaempleados': consultaempleados})

def crearempleado(request):
    if request.method == 'POST':
        empleado.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            correo=request.POST['correo'],
            telefono=request.POST['telefono']
        )
    return redirect('/pageempleados/')