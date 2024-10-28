from django.db import models

class integrante(models.Model):
    nombre = models.CharField(max_length= 100)
    rut = models.CharField(max_length= 100)
    edad = models.IntegerField()
    grupo = models.CharField(max_length= 100)
    cancion = models.CharField(max_length= 100)
    localidad = models.CharField(max_length= 100)
# Create your models here.
