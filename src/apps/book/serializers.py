from rest_framework import serializers

from apps.book.models import Book
from apps.borrow.models import Borrow


# Relations

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'


# Base

class BookSerializer(serializers.ModelSerializer):
    borrows = BorrowSerializer(source='borrow_set', many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    borrows = BorrowSerializer(source='borrow_set', many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
