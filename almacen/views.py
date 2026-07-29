from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventario, Sucursal
from productos.models import Producto

def listarinventarios(request):
    consulta = Inventario.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'almacen/inventarios.html', {
        'consultainventarios': consulta,
        'productos_lista': Producto.objects.filter(estatus=True),
        'sucursales_lista': Sucursal.objects.filter(estatus=True),
        'mostrar_todos': False
    })

def listar_todos_inventarios(request):
    consulta = Inventario.objects.filter(estatus=True).order_by('-id')
    return render(request, 'almacen/inventarios.html', {
        'consultainventarios': consulta,
        'productos_lista': Producto.objects.filter(estatus=True),
        'sucursales_lista': Sucursal.objects.filter(estatus=True),
        'mostrar_todos': True
    })

def crearinventario(request):
    if request.method == 'POST':
        prod_id = request.POST.get('producto_id')
        suc_id = request.POST.get('sucursal_id')
        
        prod_obj = get_object_or_404(Producto, id=prod_id)
        suc_obj = get_object_or_404(Sucursal, id=suc_id)

        Inventario.objects.create(
            producto=prod_obj,
            sucursal=suc_obj,
            cantidad=request.POST.get('cantidad', 0),
            ubicacion=request.POST.get('ubicacion', 'Piso de venta')
        )
    return redirect('/pagealmacen/')

def desactivarinventario(request, id):
    inv = get_object_or_404(Inventario, id=id)
    inv.estatus = False
    inv.save()
    return redirect('/pagealmacen/')

def editarinventario(request, id):
    inv = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        inv.cantidad = request.POST.get('cantidad')
        inv.ubicacion = request.POST.get('ubicacion')
        inv.save()
        return redirect('/pagealmacen/')
    return render(request, 'almacen/editar_inventario.html', {'inventario': inv})

def consultarinventario(request, id):
    inv = get_object_or_404(Inventario, id=id)
    return render(request, 'almacen/consultar_inventario.html', {'inventario': inv})

def listar_inactivos(request):
    consulta = Inventario.objects.filter(estatus=False).order_by('-id')
    return render(request, 'almacen/inactivos.html', {'consultainventarios': consulta})

def restaurarinventario(request, id):
    inv = get_object_or_404(Inventario, id=id)
    inv.estatus = True
    inv.save()
    return redirect('/pagealmacen/')