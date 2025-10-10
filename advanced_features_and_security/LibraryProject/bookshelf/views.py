from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book


# ✅ View all books (everyone who can view)
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})


# ✅ Add a new book (only users with can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')

        # Basic validation
        if title and author and publication_year:
            Book.objects.create(
                title=title,
                author=author,
                publication_year=publication_year
            )
            return redirect('view_books')  # ✅ redirect back to list

    return render(request, 'bookshelf/add_book.html')


# ✅ Edit existing book (only users with can_edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('view_books')

    return render(request, 'bookshelf/edit_book.html', {'book': book})


# ✅ Delete book (only users with can_delete permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('view_books')

    return render(request, 'bookshelf/delete_book.html', {'book': book})

