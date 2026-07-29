from django.shortcuts import render, redirect
from .models import Caja
from empleados.models import Empleado
from turno.models import Turno

def listarcajas(request):
    consultacajas = Caja.objects.all()
    # Traemos también empleados y turnos para llenar los selectores dinámicos del formulario
    consultaempleados = Empleado.objects.all()
    consultaturnos = Turno.objects.all()
    
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
        
        Caja.objects.create(
            numero=request.POST['numero'],
            usuario_id=id_empleado,
            turno_id=id_turno
        )
    return redirect('/pagecaja/')