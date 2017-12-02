from django.db import models
import datetime

# Create your models here.


class Asistente(models.Model):
    id = models.Autofield(primary_key=True)
    nombre = models.CharField(max_length=50)
    insumo = models.CharField()


class Posada(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.DateTimeField()
    insumos_asistentes =
