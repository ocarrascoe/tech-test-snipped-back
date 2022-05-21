from rest_framework import serializers

from apps.book.models import Book


class BookSerializer(serializers.ModelSerializer):
    """Serializes a user object for listing them all"""

    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    """Serializes a user object for listing them all"""

    class Meta:
        model = Book
        fields = '__all__'


class BookCreateSerializer(serializers.ModelSerializer):
    """Serializes a user object for listing them all"""

    class Meta:
        model = Book
        fields = '__all__'


class BookUpdateSerializer(serializers.ModelSerializer):
    """Serializes a user object for listing them all"""

    class Meta:
        model = Book
        fields = '__all__'


class BookPartialUpdateSerializer(serializers.ModelSerializer):
    """Serializes a user object for listing them all"""

    class Meta:
        model = Book
        fields = '__all__'


class BookDeleteSerializer(serializers.ModelSerializer):
    """Serializes a user object for listing them all"""

    class Meta:
        model = Book
        fields = '__all__'
