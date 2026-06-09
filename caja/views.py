from django.shortcuts import render

def caja(request):
    return render(request, 'caja/caja.html')