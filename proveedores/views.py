from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from almacen.models import Sucursal

def listarproveedores(request):
    consulta = Proveedor.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'proveedores/proveedores.html', {
        'consultaproveedores': consulta,
        'sucursales_lista': Sucursal.objects.filter(estatus=True),
        'mostrar_todos': False
    })

def listar_todos_proveedores(request):
    consulta = Proveedor.objects.filter(estatus=True).order_by('-id')
    return render(request, 'proveedores/proveedores.html', {
        'consultaproveedores': consulta,
        'sucursales_lista': Sucursal.objects.filter(estatus=True),
        'mostrar_todos': True
    })

def crearproveedor(request):
    if request.method == 'POST':
        suc_id = request.POST.get('sucursal_id')
        suc_obj = get_object_or_404(Sucursal, id=suc_id) if suc_id else None

        Proveedor.objects.create(
            nombre=request.POST.get('nombre'),
            empresa=request.POST.get('empresa'),
            telefono=request.POST.get('telefono'),
            sucursal_base=suc_obj
        )
    return redirect('/pageproveedores/')

def desactivarproveedor(request, id):
    prov = get_object_or_404(Proveedor, id=id)
    prov.estatus = False
    prov.save()
    return redirect('/pageproveedores/')

def editarproveedor(request, id):
    prov = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        prov.nombre = request.POST.get('nombre')
        prov.empresa = request.POST.get('empresa')
        prov.telefono = request.POST.get('telefono')
        
        suc_id = request.POST.get('sucursal_id')
        if suc_id:
            prov.sucursal_base = get_object_or_404(Sucursal, id=suc_id)
        
        prov.save()
        return redirect('/pageproveedores/')
    
    return render(request, 'proveedores/editar_proveedor.html', {
        'proveedor': prov,
        'sucursales_lista': Sucursal.objects.filter(estatus=True)
    })

def consultarproveedor(request, id):
    prov = get_object_or_404(Proveedor, id=id)
    return render(request, 'proveedores/consultar_proveedor.html', {'proveedor': prov})

def listar_inactivos(request):
    consulta = Proveedor.objects.filter(estatus=False).order_by('-id')
    return render(request, 'proveedores/inactivos.html', {'consultaproveedores': consulta})

def restaurarproveedor(request, id):
    prov = get_object_or_404(Proveedor, id=id)
    prov.estatus = True
    prov.save()
    return redirect('/pageproveedores/')