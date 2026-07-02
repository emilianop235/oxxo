from django.shortcuts import render

def empleado(request):
    return render(request, 'empleado/empleado.html')