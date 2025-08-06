from django.db import models
from datetime import date

# Author model: Represents a book author
class Author(models.Model):
    name = models.CharField(max_length=100)  # The author's name

    def __str__(self):
        return self.name

# Book model: Represents a book with title, year, and author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Relationship to Author

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
