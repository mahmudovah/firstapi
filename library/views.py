from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Author, Category
from .serializers import *

@api_view(['GET', 'POST'])
def book_api(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    return Response(serializer.data, status=200)


@api_view(['GET', 'POST'])
def author_api(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)

    if request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response(serializer.data, status=200)


# @api_view