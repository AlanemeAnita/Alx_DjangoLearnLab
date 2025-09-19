from django.shortcuts import render

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()   # Get all Book records
    serializer_class = BookSerializer  # Use the serializer to convert to JSON
