from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# ✅ Keep your ListAPIView (if required for listing)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ✅ Add a ViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

