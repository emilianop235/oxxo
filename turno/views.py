from django.shortcuts import render, redirect, get_object_or_404
from .models import Turno

def listarturnos(request):
    consulta = Turno.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'turno/turnos.html', {'consultaturnos': consulta, 'mostrar_todos': False})

def listar_todos_turnos(request):
    consulta = Turno.objects.filter(estatus=True).order_by('-id')
    return render(request, 'turno/turnos.html', {'consultaturnos': consulta, 'mostrar_todos': True})

def crearturno(request):
    if request.method == 'POST':
        Turno.objects.create(
            nombre=request.POST.get('nombre'),
            hora_inicio=request.POST.get('hora_inicio'),
            hora_fin=request.POST.get('hora_fin')
        )
    return redirect('/pageturnos/')

def desactivarturno(request, id):
    tur = get_object_or_404(Turno, id=id)
    tur.estatus = False
    tur.save()
    return redirect('/pageturnos/')

def editarturno(request, id):
    tur = get_object_or_404(Turno, id=id)
    if request.method == 'POST':
        tur.nombre = request.POST.get('nombre')
        tur.hora_inicio = request.POST.get('hora_inicio')
        tur.hora_fin = request.POST.get('hora_fin')
        tur.save()
        return redirect('/pageturnos/')
    return render(request, 'turno/editar_turno.html', {'turno': tur})

def consultarturno(request, id):
    tur = get_object_or_404(Turno, id=id)
    return render(request, 'turno/consultar_turno.html', {'turno': tur})

def listar_inactivos(request):
    consulta = Turno.objects.filter(estatus=False).order_by('-id')
    return render(request, 'turno/inactivos.html', {'consultaturnos': consulta})

def restaurarturno(request, id):
    tur = get_object_or_404(Turno, id=id)
    tur.estatus = True
    tur.save()
    return redirect('/pageturnos/')