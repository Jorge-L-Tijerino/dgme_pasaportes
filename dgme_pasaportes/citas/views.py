from django.shortcuts import render, redirect, get_object_or_404
from .forms import Paso1Form, Paso2Form, Paso3Form
from .models import Cita
import datetime

def home(request):
    return render(request, 'citas/home.html')

def paso1(request):
    if request.method == 'POST':
        form = Paso1Form(request.POST)
        if form.is_valid():
            request.session['paso1'] = form.cleaned_data
            return redirect('paso2')
    else:
        form = Paso1Form()
    return render(request, 'citas/paso1_datos.html', {'form': form})

def paso2(request):
    if request.method == 'POST':
        form = Paso2Form(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            # Convertir fecha y hora a string para la sesión
            request.session['paso2'] = {
                'tipo_tramite': datos['tipo_tramite'],
                'sede_sertrami': datos['sede_sertrami'],
                'fecha_cita': datos['fecha_cita'].isoformat(),  # YYYY-MM-DD
                'hora_cita': datos['hora_cita'].isoformat(),    # HH:MM:SS
            }
            return redirect('paso3')
    else:
        form = Paso2Form()
    return render(request, 'citas/paso2_agendamiento.html', {'form': form})


def paso3(request):
    if request.method == 'POST':
        form = Paso3Form(request.POST, request.FILES)
        if form.is_valid():
            paso1 = request.session.get('paso1', {})
            paso2 = request.session.get('paso2', {})
            paso3 = form.cleaned_data

            cita = Cita(
                nombres=paso1.get('nombres'),
                apellidos=paso1.get('apellidos'),
                cedula=paso1.get('cedula'),
                telefono=paso1.get('telefono'),
                correo=paso1.get('correo'),
                tipo_tramite=paso2.get('tipo_tramite'),
                sede_sertrami=paso2.get('sede_sertrami'),
                fecha_cita=datetime.date.fromisoformat(paso2.get('fecha_cita')),
                hora_cita=datetime.time.fromisoformat(paso2.get('hora_cita')),
                comprobante_pago=paso3.get('comprobante_pago'),
            )
            cita.save()
            request.session.flush()
            return redirect('confirmacion', cita_id=cita.id)
    else:
        form = Paso3Form()
    return render(request, 'citas/paso3_comprobante.html', {'form': form})

def confirmacion(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    return render(request, 'citas/confirmacion.html', {'cita': cita})



# Create your views here.
