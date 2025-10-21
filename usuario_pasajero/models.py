from django.db import models

class UsuarioPasajero(models.Model):
    id_usuario_pasajero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateField()
    
    def __str__(self):
        return self.nombre