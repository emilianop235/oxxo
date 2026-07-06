from django.shortcuts import render, redirect
from .models import turno

def listarturnos(request):
    # Consultamos a PostgreSQL los turnos configurados
    consultaturnos = turno.objects.all()
    return render(request, 'turno/turno.html', {'consultaturnos': consultaturnos})

def crearturno(request):
    if request.method == 'POST':
        turno.objects.create(
            nombre=request.POST['nombre'],
            hora_inicio=request.POST['hora_inicio'],
            hora_fin=request.POST['hora_fin']
        )
    return redirect('/pageturno/')