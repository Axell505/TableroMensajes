from django.shortcuts import render
from django.http import HttpResponse
from .models import Mensaje

def mensajes_recibidos(request):
    destinatario = request.GET.get('destinatario')  # Captura el destinatario desde los parámetros de la URL
    mensajes = Mensaje.objects.filter(destinatario=destinatario)  # Filtra los mensajes por destinatario
    return render(request, 'mensajes_recibidos.html', {'mensajes': mensajes})

def home(request):
    return HttpResponse("¡Bienvenido a la página principal!")