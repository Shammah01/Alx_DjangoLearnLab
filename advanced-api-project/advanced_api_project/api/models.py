from django.db import models
from datetime import datetime

# 🧑‍💼 Author model to represent book authors
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 📚 Book model to represent individual books
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

