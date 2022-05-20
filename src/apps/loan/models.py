from datetime import date, timedelta

from django.db import models

from apps.book.models import Book
from apps.user.models import User


class Loan(models.Model):
    numeropedido = models.AutoField(primary_key=True)
    librocodigo = models.ForeignKey(Book, on_delete=models.PROTECT)
    usuariocodigo = models.ForeignKey(User, on_delete=models.PROTECT)
    fechaprestamo = models.DateField(blank=True, null=False, default=date.today())
    fechamaximadevolucion = models.DateField(blank=True, null=False, default=(date.today() + timedelta(days=15)))
    fechadevolucion = models.DateField(blank=False, null=False)
