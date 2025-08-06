from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested representation of the author

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        