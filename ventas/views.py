from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta
from caja.models import Caja
from productos.models import Producto

def listarventas(request):
    consulta = Venta.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'ventas/ventas.html', {
        'consultaventas': consulta,
        'cajas_lista': Caja.objects.filter(estatus=True),
        'productos_lista': Producto.objects.filter(estatus=True),
        'mostrar_todos': False
    })

def listar_todas_ventas(request):
    consulta = Venta.objects.filter(estatus=True).order_by('-id')
    return render(request, 'ventas/ventas.html', {
        'consultaventas': consulta,
        'cajas_lista': Caja.objects.filter(estatus=True),
        'productos_lista': Producto.objects.filter(estatus=True),
        'mostrar_todos': True
    })

def crearventa(request):
    if request.method == 'POST':
        caja_obj = get_object_or_404(Caja, id=request.POST.get('caja_id')) if request.POST.get('caja_id') else None
        prod_obj = get_object_or_404(Producto, id=request.POST.get('producto_id'))
        
        Venta.objects.create(
            caja=caja_obj,
            producto=prod_obj,
            cantidad=request.POST.get('cantidad', 1),
            precio_unitario=request.POST.get('precio_unitario')
        )
    return redirect('/pageventas/')

def desactivarventa(request, id):
    venta_obj = get_object_or_404(Venta, id=id)
    venta_obj.estatus = False
    venta_obj.save()
    return redirect('/pageventas/')

def editarventa(request, id):
    venta_obj = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta_obj.cantidad = request.POST.get('cantidad')
        venta_obj.precio_unitario = request.POST.get('precio_unitario')
        venta_obj.save()
        return redirect('/pageventas/')
    return render(request, 'ventas/editar_venta.html', {'venta': venta_obj})

def consultarventa(request, id):
    venta_obj = get_object_or_404(Venta, id=id)
    return render(request, 'ventas/consultar_venta.html', {'venta': venta_obj})

def listar_inactivos(request):
    consulta = Venta.objects.filter(estatus=False).order_by('-id')
    return render(request, 'ventas/inactivos.html', {'consultaventas': consulta})

def restaurarventa(request, id):
    venta_obj = get_object_or_404(Venta, id=id)
    venta_obj.estatus = True
    venta_obj.save()
    return redirect('/pageventas/')