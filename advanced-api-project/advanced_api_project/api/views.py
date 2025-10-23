from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books or create a new one
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow anyone to read, only authenticated users can create
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Retrieve, update, or delete a specific book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can edit/delete
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all books and creating a new book.
    - GET: Returns a list of books (public).
    - POST: Creates a new book (authenticated users only).
    """

