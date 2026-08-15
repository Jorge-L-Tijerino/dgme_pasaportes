from django.contrib import admin
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'tipo_tramite', 'sede_sertrami', 'fecha_cita', 'hora_cita', 'codigo_confirmacion')
    search_fields = ('nombres', 'apellidos', 'cedula', 'codigo_confirmacion')
    list_filter = ('tipo_tramite', 'sede_sertrami', 'fecha_cita')
# Register your models here.
