from django.shortcuts import render

def empleado(request):
    return render(request, 'empleados/empleado.html')