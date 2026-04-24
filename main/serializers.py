from main.models import Book, Author, Category
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'year', 'num']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'sort', 'num']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        author = Author.name
        model = Book
        fields = ['id', 'title', 'price', 'author']


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id','title', 'description', 'author', 'price', 'category', 'updated_at', 'created_at']
        read_only_fields = ['updated_at', 'created_at']
        