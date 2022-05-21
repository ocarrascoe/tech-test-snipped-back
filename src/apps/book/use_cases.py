from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from apps.book import serializers
from apps.book.models import Book
from apps.book.repositories import BookRepository


class BookUseCases:
    # Set book as available (not loaned), this is not a real attribute,
    # it is just a flag to indicate if the book is available or not for frontend management.
    def set_availability(self, payload):
        print('payload: ', payload)
        print('len(payload): ', len(payload))
        if isinstance(payload, dict):
            is_available = True
            if payload['loans']:
                for loan in payload['loans']:
                    if not loan['fechadevolucion']:
                        is_available = False
            payload['is_available'] = is_available
        else:
            for book in payload:
                is_available = True
                print('book: ', book)
                if 'loans' in book.keys():
                    for loan in book['loans']:
                        if not loan['fechadevolucion']:
                            is_available = False
                book['is_available'] = is_available
        return payload

    def get_book(self, book_id: int):
        try:
            book = BookRepository.get_book(book_id)
            serialized_books = serializers.BookSerializer(book).data
            serialized_books = self.set_availability(payload=serialized_books)
            return {'data': serialized_books, 'status': status.HTTP_200_OK}
        except ObjectDoesNotExist:
            return {'data': {'error': 'Book does not exist!'}, 'status': status.HTTP_404_NOT_FOUND}

    def get_books(self):
        try:
            books = BookRepository.get_books()
            print('books: ', books)
            serialized_books = serializers.BookListSerializer(books, many=True)
            serialized_books = self.set_availability(payload=serialized_books.data)
            return {'data': serialized_books, 'status': status.HTTP_200_OK}
        except ObjectDoesNotExist:
            return {'data': {'error': 'Books not found.'}, 'status': status.HTTP_404_NOT_FOUND}

    def create_book(self, book):
        # Apply business logic here
        print('book.data: ', book.data)
        book, created = BookRepository.create_book(book.data)
        print('book: ', book)
        print('created: ', created)
        if created:
            return {'data': {'message': 'Book created.'}, 'status': status.HTTP_200_OK}
        else:
            return {'data': {'error': 'Book already exists.'}, 'status': status.HTTP_409_CONFLICT}

    def update_book(self, request, book_id: int):
        # Apply business logic here
        book = BookRepository.get_book(book_id)
        serialized_book = serializers.BookUpdateSerializer(book, data=request.data)
        if serialized_book.is_valid():
            serialized_book.save()
            return {'data': serialized_book.data, 'status': status.HTTP_200_OK}
        else:
            return {'data': serialized_book.errors, 'status': status.HTTP_400_BAD_REQUEST}

    def update_book_partially(self, request, book_id: int):
        # Apply business logic here
        book = BookRepository.get_book(book_id)
        serialized_book = serializers.BookUpdateSerializer(book, data=request.data, partial=True)
        if serialized_book.is_valid():
            serialized_book.save()
            return {'data': serialized_book.data, 'status': status.HTTP_200_OK}
        else:
            return {'data': serialized_book.errors, 'status': status.HTTP_400_BAD_REQUEST}

    def delete_book(self, book_id: int):
        # Apply business logic here
        try:
            BookRepository.delete_book(book_id)
            return {'data': {'message': 'Book deleted.'}, 'status': status.HTTP_200_OK}
        except ObjectDoesNotExist:
            return {'data': {'error': 'Book does not exist!'}, 'status': status.HTTP_404_NOT_FOUND}

    def get_available_books(self):
        try:
            books = BookRepository.get_available_books()
            serialized_books = serializers.BookListSerializer(books, many=True)
            return {'data': serialized_books.data, 'status': status.HTTP_200_OK}
        except ObjectDoesNotExist:
            return {'data': {'error': 'Books not found.'}, 'status': status.HTTP_404_NOT_FOUND}

    def get_loaned_books(self):
        try:
            books = BookRepository.get_loaned_books()
            serialized_books = serializers.BookListSerializer(books, many=True)
            return {'data': serialized_books.data, 'status': status.HTTP_200_OK}
        except ObjectDoesNotExist:
            return {'data': {'error': 'Books not found.'}, 'status': status.HTTP_404_NOT_FOUND}
