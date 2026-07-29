from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

def listarproductos(request):
    consulta = Producto.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'productos/productos.html', {'consultaproductos': consulta, 'mostrar_todos': False})

def listar_todos_productos(request):
    consulta = Producto.objects.filter(estatus=True).order_by('-id')
    return render(request, 'productos/productos.html', {'consultaproductos': consulta, 'mostrar_todos': True})

def crearproducto(request):
    if request.method == 'POST':
        Producto.objects.create(
            codigo_barras=request.POST.get('codigo_barras'),
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            precio_venta=request.POST.get('precio_venta')
        )
    return redirect('/pageproductos/')

def desactivarproducto(request, id):
    prod = get_object_or_404(Producto, id=id)
    prod.estatus = False
    prod.save()
    return redirect('/pageproductos/')

def editarproducto(request, id):
    prod = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        prod.codigo_barras = request.POST.get('codigo_barras')
        prod.nombre = request.POST.get('nombre')
        prod.descripcion = request.POST.get('descripcion')
        prod.precio_venta = request.POST.get('precio_venta')
        prod.save()
        return redirect('/pageproductos/')
    return render(request, 'productos/editar_producto.html', {'producto': prod})

def consultarproducto(request, id):
    prod = get_object_or_404(Producto, id=id)
    return render(request, 'productos/consultar_producto.html', {'producto': prod})

def listar_inactivos(request):
    consulta = Producto.objects.filter(estatus=False).order_by('-id')
    return render(request, 'productos/inactivos.html', {'consultaproductos': consulta})

def restaurarproducto(request, id):
    prod = get_object_or_404(Producto, id=id)
    prod.estatus = True
    prod.save()
    return redirect('/pageproductos/')