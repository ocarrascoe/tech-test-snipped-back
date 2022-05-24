from datetime import date, timedelta

from django.db import models
from django.utils import timezone

from apps.book.models import Book
from apps.user.models import User


def get_fechamaximadevolucion():
    return timezone.now() + timezone.timedelta(days=15)


class Borrow(models.Model):
    numeropedido = models.AutoField(primary_key=True)
    librocodigo = models.ForeignKey(Book, on_delete=models.CASCADE)
    usuariocodigo = models.ForeignKey(User, on_delete=models.CASCADE)
    fechaprestamo = models.DateField(blank=True, null=False, default=timezone.now)
    fechamaximadevolucion = models.DateField(blank=True, null=False, default=get_fechamaximadevolucion)
    fechadevolucion = models.DateField(blank=True, null=True)

