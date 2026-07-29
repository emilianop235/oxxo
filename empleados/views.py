from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado

def listarempleados(request):
    consulta = Empleado.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'empleados/empleados.html', {'consultaempleados': consulta, 'mostrar_todos': False})

def listar_todos_empleados(request):
    consulta = Empleado.objects.filter(estatus=True).order_by('-id')
    return render(request, 'empleados/empleados.html', {'consultaempleados': consulta, 'mostrar_todos': True})

def crearempleado(request):
    if request.method == 'POST':
        Empleado.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            correo=request.POST.get('correo'),
            telefono=request.POST.get('telefono')
        )
    return redirect('/pageempleados/')

def desactivarempleado(request, id):
    emp = get_object_or_404(Empleado, id=id)
    emp.estatus = False
    emp.save()
    return redirect('/pageempleados/')

def editarempleado(request, id):
    emp = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        emp.nombre = request.POST.get('nombre')
        emp.apellido = request.POST.get('apellido')
        emp.correo = request.POST.get('correo')
        emp.telefono = request.POST.get('telefono')
        emp.save()
        return redirect('/pageempleados/')
    return render(request, 'empleados/editar_empleado.html', {'empleado': emp})

def consultarempleado(request, id):
    emp = get_object_or_404(Empleado, id=id)
    return render(request, 'empleados/consultar_empleado.html', {'empleado': emp})

def listar_inactivos(request):
    consulta = Empleado.objects.filter(estatus=False).order_by('-id')
    return render(request, 'empleados/inactivos.html', {'consultaempleados': consulta})

def restaurarempleado(request, id):
    emp = get_object_or_404(Empleado, id=id)
    emp.estatus = True
    emp.save()
    return redirect('/pageempleados/')