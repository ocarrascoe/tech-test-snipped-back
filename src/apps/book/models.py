from djmoney.models.validators import MinMoneyValidator
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    codigolibro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60, blank=False)
    editorial = models.CharField(max_length=25, blank=True)
    autor = models.CharField(max_length=40, blank=False)
    genero = models.CharField(max_length=20, blank=False)
    paisautor = models.CharField(max_length=20, blank=True)
    numeropaginas = models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1)])
    anoedicion = models.CharField(max_length=5, blank=True)
    precio = MoneyField(blank=False, max_digits=14, decimal_places=2, default_currency='EUR', validators=[
        MinMoneyValidator(1),
    ])
