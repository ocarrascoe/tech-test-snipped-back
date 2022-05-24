from django.utils import timezone

from apps.borrow.models import Borrow


class BorrowRepository:
    @staticmethod
    def create_borrow(user, book) -> Borrow:
        return Borrow.objects.create(usuariocodigo=user, librocodigo=book)

    @staticmethod
    def return_book(user_id, book_id) -> Borrow:
        return Borrow.objects.filter(usuariocodigo_id=user_id, librocodigo_id=book_id, fechadevolucion=None).update(
            fechadevolucion=timezone.now())
