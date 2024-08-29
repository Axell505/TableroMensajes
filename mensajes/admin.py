from django.contrib import admin
from .models import Mensaje

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('texto', 'remitente', 'destinatario', 'fecha_y_hora')
    search_fields = ('texto', 'remitente', 'destinatario')
