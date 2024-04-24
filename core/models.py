from django.db import models

# Create your models here.


class Carros(models.Model):
	matricula = models.CharField(max_length=7, unique=True)
	destino = models.CharField(max_length=50)
	cant_paquetes = models.PositiveSmallIntegerField()

	def __str__(self):
		texto = "{0} ({1})"
		return texto.format(self.matricula, self.cant_paquetes)