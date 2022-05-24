from django.utils import timezone

from apps.borrow.models import Borrow


class BorrowRepository:
    @staticmethod
    def create_borrow(user, book) -> Borrow:
        return Borrow.objects.create(usuariocodigo=user, librocodigo=book)

    @staticmethod
    def return_book(book_id) -> Borrow:
        return Borrow.objects.filter(librocodigo_id=book_id, fechadevolucion__isnull=True).update(
            fechadevolucion=timezone.now())
