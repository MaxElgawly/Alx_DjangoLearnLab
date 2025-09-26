from django.db import models

# Author model represents a writer with one-to-many relationship to Book.
class Author(models.Model):
    name = models.CharField(max_length=255)  # stores author’s name

    def __str__(self):
        return self.name


# Book model represents books written by an Author.
class Book(models.Model):
    title = models.CharField(max_length=255)  # book title
    publication_year = models.IntegerField()  # year published
    # One author can have many books. CASCADE deletes all books if author deleted.
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Create your models here.
