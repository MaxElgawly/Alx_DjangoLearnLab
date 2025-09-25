from django.db import models

# Author model represents a writer who may have multiple books.
class Author(models.Model):
    name = models.CharField(max_length=255)  # store author's name

    def __str__(self):
        return self.name

# Book model represents an individual book written by an Author.
class Book(models.Model):
    title = models.CharField(max_length=255)              # book title
    publication_year = models.IntegerField()              # year published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    # related_name='books' allows accessing all books of an author via author.books.all()

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

# Create your models here.
