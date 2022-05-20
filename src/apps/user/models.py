from django.db import models


class User(models.Model):
    codigousuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15, blank=False, null=False)
    apellido1 = models.CharField(max_length=20, blank=False, null=False)
    apellido2 = models.CharField(max_length=20, blank=True, null=True)
    fechanacimiento = models.DateField(blank=False, null=False)
    dni = models.CharField(max_length=12, blank=True, null=True)
    domicilio = models.CharField(max_length=50, blank=False, null=False)
    poblacion = models.CharField(max_length=30, blank=True, null=True)
    provincia = models.CharField(max_length=20, blank=True, null=True)
