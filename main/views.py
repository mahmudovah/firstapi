from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Book, Author, Category
from main.serializers import BookSerializer, AuthorSerializer, CategorySerializer, BookDetailSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET','POST'])
def first_api(request):
    return Response({
        'success' : 'True',
        'message' : 'API gamurojat',
        'method' : request.method
    })


@api_view(['GET', 'POST'])
def books_api(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def category_api(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)

    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    return Response(serializer.data, status=200)


@api_view(['GET','POST'])
def author_api(request):
    auth = Author.objects.all()
    serializer = AuthorSerializer(auth, many=True)

    if request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    return Response(serializer.data, status=200)


@api_view(['GET', 'PATCH'])
def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)

    serializer = BookDetailSerializer(book)

    if request.method == 'PATCH':
        serializer = BookDetailSerializer(book, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        serializer.save()
        return Response(serializer.data, status=200)
    
    return Response(serializer.data, status=200)

@api_view(['GET'])
def me_api(request):
    if not request.user.is_authenticated:
        return Response({
            'success': False,
            'message': 'siz tizimga kirmagansiz!'
        })
    
    user = request.user
    return Response({
        'user': user.username
    })