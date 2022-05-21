from rest_framework import serializers

from apps.book.models import Book
from apps.loan.models import Loan


# Relations

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'


# Base

class BookSerializer(serializers.ModelSerializer):
    loans = LoanSerializer(source='loan_set', many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    loans = LoanSerializer(source='loan_set', many=True)

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
