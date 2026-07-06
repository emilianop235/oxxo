from django.shortcuts import render, redirect
from .models import caja
from empleados.models import empleado
from turno.models import turno

def listarcajas(request):
    consultacajas = caja.objects.all()
    # Traemos también empleados y turnos para llenar los selectores dinámicos del formulario
    consultaempleados = empleado.objects.all()
    consultaturnos = turno.objects.all()
    
    context = {
        'consultacajas': consultacajas,
        'consultaempleados': consultaempleados,
        'consultaturnos': consultaturnos
    }
    return render(request, 'caja/caja.html', context)

def crearcaja(request):
    if request.method == 'POST':
        # Obtenemos las llaves foráneas usando los IDs enviados por el <select>
        id_empleado = request.POST['usuario']
        id_turno = request.POST['turno']
        
        caja.objects.create(
            numero=request.POST['numero'],
            usuario_id=id_empleado,
            turno_id=id_turno
        )
    return redirect('/pagecaja/')