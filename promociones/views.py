from django.shortcuts import render, redirect, get_object_or_404
from .models import Promocion
from productos.models import Producto

def listarpromociones(request):
    consulta = Promocion.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'promociones/promociones.html', {
        'consultapromociones': consulta,
        'productos_lista': Producto.objects.filter(estatus=True),
        'mostrar_todos': False
    })

def listar_todas_promociones(request):
    consulta = Promocion.objects.filter(estatus=True).order_by('-id')
    return render(request, 'promociones/promociones.html', {
        'consultapromociones': consulta,
        'productos_lista': Producto.objects.filter(estatus=True),
        'mostrar_todos': True
    })

def crearpromocion(request):
    if request.method == 'POST':
        prod_obj = get_object_or_404(Producto, id=request.POST.get('producto_id'))

        Promocion.objects.create(
            nombre_promo=request.POST.get('nombre_promo'),
            producto_en_promocion=prod_obj,
            porcentaje_descuento=request.POST.get('porcentaje_descuento'),
            fecha_inicio=request.POST.get('fecha_inicio'),
            fecha_fin=request.POST.get('fecha_fin')
        )
    return redirect('/pagepromociones/')

def desactivarpromocion(request, id):
    promo = get_object_or_404(Promocion, id=id)
    promo.estatus = False
    promo.save()
    return redirect('/pagepromociones/')

def editarpromocion(request, id):
    promo = get_object_or_404(Promocion, id=id)
    if request.method == 'POST':
        promo.nombre_promo = request.POST.get('nombre_promo')
        promo.porcentaje_descuento = request.POST.get('porcentaje_descuento')
        promo.fecha_inicio = request.POST.get('fecha_inicio')
        promo.fecha_fin = request.POST.get('fecha_fin')
        promo.save()
        return redirect('/pagepromociones/')
        
    return render(request, 'promociones/editar_promocion.html', {'promocion': promo})

def consultarpromocion(request, id):
    promo = get_object_or_404(Promocion, id=id)
    return render(request, 'promociones/consultar_promocion.html', {'promocion': promo})

def listar_inactivos(request):
    consulta = Promocion.objects.filter(estatus=False).order_by('-id')
    return render(request, 'promociones/inactivos.html', {'consultapromociones': consulta})

def restaurarpromocion(request, id):
    promo = get_object_or_404(Promocion, id=id)
    promo.estatus = True
    promo.save()
    return redirect('/pagepromociones/')