from django.shortcuts import render

def turno(request):
    return render(request, 'turno/turno.html')