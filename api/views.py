from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def listbooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addbook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def bookdetails(request, isbn):
    try:
        book = Book.objects.get(isbn=isbn)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response(status=404)

@api_view(['PUT'])
def updatebook(request, isbn):
    try:
        book = Book.objects.get(isbn=isbn)
    except Book.DoesNotExist:
        return Response(status=404)
    
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deletebook(request, isbn):
    try:
        book = Book.objects.get(isbn=isbn)
    except Book.DoesNotExist:
        return Response(status=404)
    
    book.delete()
    return Response(status=204)
