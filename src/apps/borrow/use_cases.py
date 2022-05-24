from rest_framework import status

from apps.book.models import Book
from apps.borrow.repositories import BorrowRepository
from apps.user.models import User


class BorrowUseCases:

    def create_borrow(self, user_id, book_id):
        # Apply business logic here
        user = User.objects.filter(codigousuario=user_id).get()
        book = Book.objects.filter(codigolibro=book_id).get()
        book = BorrowRepository.create_borrow(user, book)
        return {'data': {'message': 'Borrow created.'}, 'status': status.HTTP_200_OK}

    def return_book(self, user_id, book_id):
        # Apply business logic here
        book = BorrowRepository.return_book(user_id, book_id)
        return {'data': {'message': 'Book returned.'}, 'status': status.HTTP_200_OK}
