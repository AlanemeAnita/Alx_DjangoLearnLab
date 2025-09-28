# advanced-api-project/api/views.py

"""
Generic views for Book model:
- BookListView: list all books (GET)  --> public (AllowAny)
- BookDetailView: retrieve a single book (GET) --> public (AllowAny)
- BookCreateView: create a new book (POST) --> authenticated users only
- BookUpdateView: update an existing book (PUT/PATCH) --> authenticated users only
- BookDeleteView: delete a book (DELETE) --> authenticated users only

We also demonstrate simple search & ordering on the list view.
"""

from rest_framework import generics, permissions, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
