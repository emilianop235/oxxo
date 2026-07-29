from django.shortcuts import render, redirect, get_object_or_404
from .models import Caja
from empleados.models import Empleado
from turno.models import Turno
from almacen.models import Sucursal

def listarcajas(request):
    consulta = Caja.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'caja/cajas.html', {
        'consultacajas': consulta,
        'empleados_lista': Empleado.objects.filter(estatus=True),
        'turnos_lista': Turno.objects.filter(estatus=True),
        'sucursales_lista': Sucursal.objects.filter(estatus=True),
        'mostrar_todos': False
    })

def listar_todas_cajas(request):
    consulta = Caja.objects.filter(estatus=True).order_by('-id')
    return render(request, 'caja/cajas.html', {
        'consultacajas': consulta,
        'empleados_lista': Empleado.objects.filter(estatus=True),
        'turnos_lista': Turno.objects.filter(estatus=True),
        'sucursales_lista': Sucursal.objects.filter(estatus=True),
        'mostrar_todos': True
    })

def crearcaja(request):
    if request.method == 'POST':
        emp_obj = get_object_or_404(Empleado, id=request.POST.get('usuario_id'))
        tur_obj = get_object_or_404(Turno, id=request.POST.get('turno_id'))
        suc_obj = get_object_or_404(Sucursal, id=request.POST.get('sucursal_id')) if request.POST.get('sucursal_id') else None

        Caja.objects.create(
            numero=request.POST.get('numero'),
            usuario=emp_obj,
            turno=tur_obj,
            sucursal=suc_obj
        )
    return redirect('/pagecaja/')

def desactivarcaja(request, id):
    caja_obj = get_object_or_404(Caja, id=id)
    caja_obj.estatus = False
    caja_obj.save()
    return redirect('/pagecaja/')

def editarcaja(request, id):
    caja_obj = get_object_or_404(Caja, id=id)
    if request.method == 'POST':
        caja_obj.numero = request.POST.get('numero')
        
        # Actualizar relaciones si se enviaron en el formulario
        if request.POST.get('usuario_id'):
            caja_obj.usuario = get_object_or_404(Empleado, id=request.POST.get('usuario_id'))
        if request.POST.get('turno_id'):
            caja_obj.turno = get_object_or_404(Turno, id=request.POST.get('turno_id'))
            
        caja_obj.save()
        return redirect('/pagecaja/')
    
    return render(request, 'caja/editar_caja.html', {
        'caja': caja_obj,
        'empleados_lista': Empleado.objects.filter(estatus=True),
        'turnos_lista': Turno.objects.filter(estatus=True)
    })

def consultarcaja(request, id):
    caja_obj = get_object_or_404(Caja, id=id)
    return render(request, 'caja/consultar_caja.html', {'caja': caja_obj})

def listar_inactivos(request):
    consulta = Caja.objects.filter(estatus=False).order_by('-id')
    return render(request, 'caja/inactivos.html', {'consultacajas': consulta})

def restaurarcaja(request, id):
    caja_obj = get_object_or_404(Caja, id=id)
    caja_obj.estatus = True
    caja_obj.save()
    return redirect('/pagecaja/')