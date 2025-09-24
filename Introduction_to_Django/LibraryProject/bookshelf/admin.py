from django.contrib import admin
from .models import Book

# Customize admin display
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show in list view
    search_fields = ('title', 'author')  # enable search
    list_filter = ('publication_year',)  # add filter sidebar

# Register Book with custom admin
admin.site.register(Book, BookAdmin)

