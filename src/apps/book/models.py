from djmoney.models.validators import MinMoneyValidator
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    codigolibro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60, blank=False, null=False)
    editorial = models.CharField(max_length=25, blank=True, null=True)
    autor = models.CharField(max_length=40, blank=False, null=False)
    genero = models.CharField(max_length=20, blank=False, null=False)
    paisautor = models.CharField(max_length=20, blank=True, null=True)
    numeropaginas = models.PositiveIntegerField(blank=False, null=False, validators=[MinValueValidator(1)])
    anoedicion = models.CharField(max_length=5, blank=True, null=True)
    precio = MoneyField(blank=False, null=False, max_digits=14, decimal_places=2, default_currency='EUR', validators=[
        MinMoneyValidator(1),
    ])
