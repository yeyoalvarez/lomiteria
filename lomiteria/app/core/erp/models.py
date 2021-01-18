from django.db import models

# Create your models here.

class persona(models.Model):
    id = models.DecimalField(default=0)
    ci = models.DecimalField(default=0)
    ruc = models.DecimalField(default=0)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)