from rest_framework import serializers
from .models import Category, Author, Book

class BookSerializer(serializers.ModelSerializer):
    author = Author.name
   # category = Category.title
    class Meta:
        model = Book
        fields = ['id', 'category', 'author','name','year']
        read_only_fields = ['category']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','birth']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']
