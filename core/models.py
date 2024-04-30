from django.db import models

class Carros(models.Model):
    matricula = models.CharField(max_length=7, primary_key=True)
    modelo = models.CharField(max_length=50)
    anioFabricacion = models.IntegerField(default=0)
    cargaActual = models.IntegerField(default=100)
    estadoCarga = models.CharField(max_length=50,default='Descargando')
    estado = models.CharField(max_length=50, default='Activo')

class Envios(models.Model):
    id_envio = models.AutoField(primary_key=True)
    paquetes_pequeños = models.PositiveSmallIntegerField(default=0)
    paquetes_grandes = models.IntegerField(default=0)
    paquetes_fragiles = models.IntegerField(default=0)
    destino = models.CharField(max_length=50)
    vehiculo_asignado = models.CharField(max_length=50,default="-")
    estado = models.CharField(max_length=50, default='Asignado')
    
    
    
    def __str__(self):
        return f"{self.matricula} ({self.paquetes_pequeños})"
