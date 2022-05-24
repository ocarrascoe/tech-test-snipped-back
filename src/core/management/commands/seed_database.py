from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from core.management.data import *

from apps.book.models import Book
from apps.borrow.models import Borrow
from apps.user.models import User

# python manage.py seed --mode=refresh
# python manage.py seed --mode=clear

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', nargs='+', type=str, help="Mode")

    def handle(self, *args, **options):
        run_seed(self, options['mode'])
        self.stdout.write('Done.')


def clear_data():
    """Deletes all the table data"""
    User.objects.all().delete()
    Borrow.objects.all().delete()
    Book.objects.all().delete()


def create_users():
    print('Creating users...')
    for user in users:
        user = User(**user)
        user.save()
    print('Users created.')


def create_books():
    print('Creating books...')
    for book in books:
        book = Book(**book)
        book.save()
    print('Books created.')


def create_borrows():
    print('Creating borrows...')
    user = User.objects.filter(nombre='Omar').get()
    book = Book.objects.filter(titulo='Don Quixote').get()
    borrow = Borrow(librocodigo=book, usuariocodigo=user)
    borrow.save()
    print('Borrows created.')


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables

    mode = mode[0]
    if mode == MODE_CLEAR:
        clear_data()

    # Seed
    print('Seeding data...')
    user = User.objects.filter(nombre='Omar')
    if len(user) > 0:
        print('Database is already seeded')
    else:
        create_users()
        create_books()
        create_borrows()
    return
