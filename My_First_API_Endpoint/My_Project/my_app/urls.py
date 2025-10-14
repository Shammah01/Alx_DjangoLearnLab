from django.urls import path
from .views import BookListCreateAPIView   # ✅ Import the view directly

urlpatterns = [
    path("api/books/", BookListCreateAPIView.as_view(), name="book_list_create"),  # ✅ Fixed
]

