from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from almacen.models import Sucursal

def listarclientes(request):
    consulta = Cliente.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'clientes/clientes.html', {
        'consultaclientes': consulta,
        'sucursales_lista': Sucursal.objects.filter(estatus=True),
        'mostrar_todos': False
    })

def listar_todos_clientes(request):
    consulta = Cliente.objects.filter(estatus=True).order_by('-id')
    return render(request, 'clientes/clientes.html', {
        'consultaclientes': consulta,
        'sucursales_lista': Sucursal.objects.filter(estatus=True),
        'mostrar_todos': True
    })

def crearcliente(request):
    if request.method == 'POST':
        suc_id = request.POST.get('sucursal_id')
        suc_obj = get_object_or_404(Sucursal, id=suc_id) if suc_id else None

        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            telefono=request.POST.get('telefono'),
            puntos_acumulados=request.POST.get('puntos_acumulados', 0),
            tienda_registro=suc_obj
        )
    return redirect('/pageclientes/')

def desactivarcliente(request, id):
    cli = get_object_or_404(Cliente, id=id)
    cli.estatus = False
    cli.save()
    return redirect('/pageclientes/')

def editarcliente(request, id):
    cli = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cli.nombre = request.POST.get('nombre')
        cli.telefono = request.POST.get('telefono')
        cli.puntos_acumulados = request.POST.get('puntos_acumulados')
        cli.save()
        return redirect('/pageclientes/')
        
    return render(request, 'clientes/editar_cliente.html', {'cliente': cli})

def consultarcliente(request, id):
    cli = get_object_or_404(Cliente, id=id)
    return render(request, 'clientes/consultar_cliente.html', {'cliente': cli})

def listar_inactivos(request):
    consulta = Cliente.objects.filter(estatus=False).order_by('-id')
    return render(request, 'clientes/inactivos.html', {'consultaclientes': consulta})

def restaurarcliente(request, id):
    cli = get_object_or_404(Cliente, id=id)
    cli.estatus = True
    cli.save()
    return redirect('/pageclientes/')