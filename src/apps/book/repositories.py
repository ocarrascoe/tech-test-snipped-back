from typing import List

from apps.book.models import Book


class BookRepository:
    @staticmethod
    def get_books() -> List[Book]:
        return Book.objects.filter(eliminado=False).all()

    @staticmethod
    def get_available_books() -> List[Book]:
        return Book.objects.exclude(loan__isnull=False).filter(eliminado=False).all()

    @staticmethod
    def get_loaned_books() -> List[Book]:
        return Book.objects.exclude(loan__isnull=True).filter(eliminado=False).all()

    @staticmethod
    def get_book(book_id: int) -> Book:
        return Book.objects.get(codigolibro=book_id)

    @staticmethod
    def create_book(book) -> Book:
        return Book.objects.get_or_create(
            titulo=book['titulo'],
            editorial=book['editorial'],
            autor=book['autor'],
            defaults={
                "titulo": book['titulo'],
                "editorial": book['editorial'],
                "autor": book['autor'],
                "genero": book['genero'],
                "paisautor": book['paisautor'],
                "numeropaginas": book['numeropaginas'],
                "anoedicion": book['anoedicion'],
                "precio": book['precio'],
            }
        )

    @staticmethod
    def update_book(book_id: int, book) -> Book:
        return Book.objects.filter(codigolibro=book_id).update(**book)

    @staticmethod
    def delete_book(book_id: int) -> Book:
        return Book.objects.filter(codigolibro=book_id).update(eliminado=True)
        # return Book.objects.filter(codigolibro=book_id).delete()
