from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.book import serializers
from apps.book.use_cases import BookUseCases
from apps.book.models import Book


class BookView(APIView):
    # Get book by its id
    def get(self, book_id, format=None):
        response = BookUseCases().get_book(book_id=book_id)
        return Response(response['data'], status=response['status'])

    # Update all book
    def put(self, request, book_id, format=None):
        response = BookUseCases().update_book(request=request, book_id=book_id)
        return Response(response['data'], status=response['status'])

    # Update book partially
    def patch(self, request, book_id, format=None):
        response = BookUseCases().update_book_partially(request=request, book_id=book_id)
        return Response(response['data'], status=response['status'])

    # Delete book by its id
    def delete(self, request, book_id, format=None):
        response = BookUseCases().delete_book(book_id=book_id)
        return Response(response['data'], status=response['status'])


class BookListView(APIView):
    # Get all books
    def get(self, format=None):
        response = BookUseCases().get_books()
        return Response(response['data'], status=response['status'])


class BookDetailView(APIView):
    # Create new book
    def post(self, request, format=None):
        response = BookUseCases().create_book(book=request)
        return Response(response['data'], status=response['status'])


class BookAvailableListView(APIView):
    def get(self, format=None):
        response = BookUseCases().get_available_books()
        return Response(response['data'], status=response['status'])


class BookLoanedListView(APIView):
    def get(self, format=None):
        response = BookUseCases().get_loaned_books()
        return Response(response['data'], status=response['status'])
