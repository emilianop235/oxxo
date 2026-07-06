from django.shortcuts import render, redirect
from .models import ventas

def listarventas(request):
    # Consultamos el historial de tickets ordenados desde el más nuevo al más antiguo
    consultaventas = ventas.objects.all().order_by('-fecha_venta')
    return render(request, 'ventas/ventas.html', {'consultaventas': consultaventas})

def crearventa(request):
    if request.method == 'POST':
        ventas.objects.create(
            producto=request.POST['producto'],
            cantidad=request.POST['cantidad'],
            precio_unitario=request.POST['precio_unitario']
        )
    return redirect('/pageventas/')