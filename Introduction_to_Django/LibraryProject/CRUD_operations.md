# CRUD Operations in Django

This document summarizes the Create, Read, Update, and Delete operations using Django’s ORM.

## 1. Create

```bash
python3 manage.py shell
```

```python
from bookshelf.models import Book

book1 = Book(title="The Alchemist", author="Paulo Coelho", published_year=1988)
book1.save()
```

**Output:**

```python
>>> book1
<Book: The Alchemist>
```

## 2. Read

```bash
python3 manage.py shell
```

```python
from bookshelf.models import Book

books = Book.objects.all()
print(books)

books_by_author = Book.objects.filter(author="Paulo Coelho")
print(books_by_author)
```

**Output:**

```python
<QuerySet [<Book: The Alchemist>]>
<QuerySet [<Book: The Alchemist>]>
```

## 3. Update

```bash
python3 manage.py shell
```

```python
from bookshelf.models import Book

book = Book.objects.get(title="The Alchemist")
book.title = "The Alchemist (Updated)"
book.save()
```

**Output:**

```python
>>> book
<Book: The Alchemist (Updated)>
```

## 4. Delete

```bash
python3 manage.py shell
```

```python
from bookshelf.models import Book

book = Book.objects.get(title="The Alchemist (Updated)")
book.delete()
```

**Output:**

```python
>>> book
(<Book: The Alchemist (Updated)>, True)
```

