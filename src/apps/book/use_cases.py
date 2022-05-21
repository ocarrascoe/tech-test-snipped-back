from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from apps.book import serializers
from apps.book.models import Book
from apps.book.repositories import BookRepository


class BookUseCases:
    @staticmethod
    def get_book(book_id: int):
        try:
            book = BookRepository.get_book(book_id)
            book_serialized = serializers.BookSerializer(book)
            return {'data': book_serialized.data, 'status': status.HTTP_200_OK}
        except ObjectDoesNotExist:
            return {'data': {'error': 'Book does not exist!'}, 'status': status.HTTP_404_NOT_FOUND}

    @staticmethod
    def get_books():
        try:
            books = BookRepository.get_books()
            print('books: ', books)
            serialized_books = serializers.BookListSerializer(books, many=True)
            return {'data': serialized_books.data, 'status': status.HTTP_200_OK}
        except ObjectDoesNotExist:
            return {'data': {'error': 'Books not found.'}, 'status': status.HTTP_404_NOT_FOUND}

    @staticmethod
    def create_book(book):
        # Apply business logic here
        print('book.data: ', book.data)
        book, created = BookRepository.create_book(book.data)
        print('book: ', book)
        print('created: ', created)
        if created:
            return {'data': {'message': 'Book created.'}, 'status': status.HTTP_200_OK}
        else:
            return {'data': {'error': 'Book already exists.'}, 'status': status.HTTP_409_CONFLICT}

    @staticmethod
    def update_book(request, book_id: int):
        # Apply business logic here
        book = BookRepository.get_book(book_id)
        serialized_book = serializers.BookUpdateSerializer(book, data=request.data)
        if serialized_book.is_valid():
            serialized_book.save()
            return {'data': serialized_book.data, 'status': status.HTTP_200_OK}
        else:
            return {'data': serialized_book.errors, 'status': status.HTTP_400_BAD_REQUEST}

    @staticmethod
    def update_book_partially(request, book_id: int):
        # Apply business logic here
        book = BookRepository.get_book(book_id)
        serialized_book = serializers.BookUpdateSerializer(book, data=request.data, partial=True)
        if serialized_book.is_valid():
            serialized_book.save()
            return {'data': serialized_book.data, 'status': status.HTTP_200_OK}
        else:
            return {'data': serialized_book.errors, 'status': status.HTTP_400_BAD_REQUEST}

    @staticmethod
    def delete_book(book_id: int):
        # Apply business logic here
        try:
            BookRepository.delete_book(book_id)
            return {'data': {'message': 'Book deleted.'}, 'status': status.HTTP_200_OK}
        except ObjectDoesNotExist:
            return {'data': {'error': 'Book does not exist!'}, 'status': status.HTTP_404_NOT_FOUND}

    @staticmethod
    def get_available_books():
        try:
            books = BookRepository.get_available_books()
            serialized_books = serializers.BookListSerializer(books, many=True)
            return {'data': serialized_books.data, 'status': status.HTTP_200_OK}
        except ObjectDoesNotExist:
            return {'data': {'error': 'Books not found.'}, 'status': status.HTTP_404_NOT_FOUND}

    @staticmethod
    def get_loaned_books():
        try:
            books = BookRepository.get_loaned_books()
            serialized_books = serializers.BookListSerializer(books, many=True)
            return {'data': serialized_books.data, 'status': status.HTTP_200_OK}
        except ObjectDoesNotExist:
            return {'data': {'error': 'Books not found.'}, 'status': status.HTTP_404_NOT_FOUND}
