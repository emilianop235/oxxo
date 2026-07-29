from django.shortcuts import render, redirect
from .models import Turno

def listarturnos(request):
    # Consultamos a PostgreSQL los turnos configurados
    consultaturnos = Turno.objects.all()
    return render(request, 'turno/turno.html', {'consultaturnos': consultaturnos})

def crearturno(request):
    if request.method == 'POST':
        Turno.objects.create(
            nombre=request.POST['nombre'],
            hora_inicio=request.POST['hora_inicio'],
            hora_fin=request.POST['hora_fin']
        )
    return redirect('/pageturno/')