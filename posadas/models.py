from django.db import models

# Create your models here.

INSUMOS = (
    ('RFCO', 'Refrescos'),
    ('PPS', 'Papas'),
    ('TST', 'Tostadas'),
    ('VS', 'Vasos'),
    ('PL', 'Platos')
)


class Posada(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.DateTimeField()


class Asistente(models.Model):
    id = models.Autofield(primary_key=True)
    nombre = models.CharField(max_length=50)
    posada = models.ForeignKey(Posada, on_delete=models.CASCADE, related_name="asistentes")
    insumo = models.CharField(max_length=50, choices=INSUMOS)
