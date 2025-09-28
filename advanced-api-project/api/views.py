# advanced-api-project/api/views.py

"""
Generic views for Book model:
- BookListView: list all books (GET)  --> public (AllowAny)
- BookDetailView: retrieve a single book (GET) --> public (AllowAny)
- BookCreateView: create a new book (POST) --> authenticated users only
- BookUpdateView: update an existing book (PUT/PATCH) --> authenticated users only
- BookDeleteView: delete a book (DELETE) --> authenticated users only
"""

from django_filters import rest_framework
from rest_framework import generics, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # ✅ REQUIRED IMPORT

from .models import Book
from .serializers import BookSerializer


# -----------------------
# READ-ONLY views (public)
# -----------------------
class BookListView(generics.ListAPIView):
    """GET /api/books/ - List all books (public)
        Supports:
      - filtering by exact fields: ?title=..., ?author=..., ?publication_year=...
      - searching text:          ?search=partialTitleOrAuthor
      - ordering results:        ?ordering=title or ?ordering=-publication_year
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'publication_year']
    # Allow read-only for everyone
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    """GET /api/books/<pk>/ - Retrieve single book (public)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -----------------------
# WRITE views (authenticated)
# -----------------------
class BookCreateView(generics.CreateAPIView):
    """POST /api/books/create/ - Create book (authenticated only)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]  # ✅ Auth required


class BookUpdateView(generics.UpdateAPIView):
    """PUT/PATCH /api/books/<pk>/update/ - Update book (authenticated only)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]  # ✅ Auth required


class BookDeleteView(generics.DestroyAPIView):
    """DELETE /api/books/<pk>/delete/ - Delete book (authenticated only)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]  # ✅ Auth required
