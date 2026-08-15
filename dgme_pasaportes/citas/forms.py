from django import forms
from .models import Cita

class Paso1Form(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombres', 'apellidos', 'cedula', 'telefono', 'correo']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class Paso2Form(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['tipo_tramite', 'sede_sertrami', 'fecha_cita', 'hora_cita']
        widgets = {
            'tipo_tramite': forms.Select(attrs={'class': 'form-select'}),
            'sede_sertrami': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_cita': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_cita': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class Paso3Form(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['comprobante_pago']
        widgets = {
            'comprobante_pago': forms.FileInput(attrs={'class': 'form-control'}),
        }
