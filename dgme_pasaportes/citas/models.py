import random
import string
from django.db import models

def generar_codigo_confirmacion():
    """Genera un código único tipo DGME-XXXXXX"""
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"DGME-{codigo}"

class Cita(models.Model):
    # Datos Personales
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=14, unique=True)  # Ejemplo: 001-120394-0000X
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    # Datos del Trámite y Cita
    TIPO_TRAMITE_CHOICES = [
        ('NUEVO', 'Pasaporte Nuevo'),
        ('RENOVACION', 'Renovación'),
        ('REPOSICION', 'Reposición'),
    ]
    tipo_tramite = models.CharField(max_length=20, choices=TIPO_TRAMITE_CHOICES)
    sede_sertrami = models.CharField(max_length=50)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()

    # Subida de Archivos
    comprobante_pago = models.FileField(upload_to='comprobantes/')

    # Gestión del Sistema
    codigo_confirmacion = models.CharField(max_length=15, unique=True, editable=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.codigo_confirmacion:
            # Genera un código único antes de guardar
            nuevo_codigo = generar_codigo_confirmacion()
            while Cita.objects.filter(codigo_confirmacion=nuevo_codigo).exists():
                nuevo_codigo = generar_codigo_confirmacion()
            self.codigo_confirmacion = nuevo_codigo
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.codigo_confirmacion}"




# Create your models here.
