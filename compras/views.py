from django.shortcuts import render, redirect, get_object_or_404
from .models import Compra
from proveedores.models import Proveedor
from productos.models import Producto
from empleados.models import Empleado

def listarcompras(request):
    consulta = Compra.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'compras/compras.html', {
        'consultacompras': consulta,
        'proveedores_lista': Proveedor.objects.filter(estatus=True),
        'productos_lista': Producto.objects.filter(estatus=True),
        'empleados_lista': Empleado.objects.filter(estatus=True),
        'mostrar_todos': False
    })

def listar_todas_compras(request):
    consulta = Compra.objects.filter(estatus=True).order_by('-id')
    return render(request, 'compras/compras.html', {
        'consultacompras': consulta,
        'proveedores_lista': Proveedor.objects.filter(estatus=True),
        'productos_lista': Producto.objects.filter(estatus=True),
        'empleados_lista': Empleado.objects.filter(estatus=True),
        'mostrar_todos': True
    })

def crearcompra(request):
    if request.method == 'POST':
        prov_obj = get_object_or_404(Proveedor, id=request.POST.get('proveedor_id'))
        prod_obj = get_object_or_404(Producto, id=request.POST.get('producto_id'))
        
        emp_id = request.POST.get('empleado_id')
        emp_obj = get_object_or_404(Empleado, id=emp_id) if emp_id else None

        Compra.objects.create(
            proveedor=prov_obj,
            producto=prod_obj,
            recibido_por=emp_obj,
            cantidad_comprada=request.POST.get('cantidad_comprada'),
            costo_total=request.POST.get('costo_total')
        )
    return redirect('/pagecompras/')

def desactivarcompra(request, id):
    compra = get_object_or_404(Compra, id=id)
    compra.estatus = False
    compra.save()
    return redirect('/pagecompras/')

def editarcompra(request, id):
    compra = get_object_or_404(Compra, id=id)
    if request.method == 'POST':
        compra.cantidad_comprada = request.POST.get('cantidad_comprada')
        compra.costo_total = request.POST.get('costo_total')
        compra.save()
        return redirect('/pagecompras/')
        
    return render(request, 'compras/editar_compra.html', {'compra': compra})

def consultarcompra(request, id):
    compra = get_object_or_404(Compra, id=id)
    return render(request, 'compras/consultar_compra.html', {'compra': compra})

def listar_inactivos(request):
    consulta = Compra.objects.filter(estatus=False).order_by('-id')
    return render(request, 'compras/inactivos.html', {'consultacompras': consulta})

def restaurarcompra(request, id):
    compra = get_object_or_404(Compra, id=id)
    compra.estatus = True
    compra.save()
    return redirect('/pagecompras/')