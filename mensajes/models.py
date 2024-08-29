from django.db import models
import datetime

class Mensaje(models.Model):
    texto = models.TextField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    fecha_y_hora = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.texto[:20]} - {self.remitente} a {self.destinatario}"
