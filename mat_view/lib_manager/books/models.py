from django.db import models
from django.utils.translation import gettext_lazy as _

class Author(models.Model):
    name = models.CharField(max_length=120)
    date_of_birth = models.DateField(null=False)
    date_of_death = models.DateField('Died', null=True, blank=True)


class Genre(models.Model):
    class GenreChoices(models.TextChoices):
        HORROR = 'HR', _("Horror")
        ADVENTURE = 'AD', _("Adventure")
        FICTION = 'FC', _("Fiction")
        NOVEL = 'NV', _("Novel")
        HISTORY = 'HS', _("History")
        THRILLER = 'TH', _("Thriller")

    name = models.CharField(choices=(GenreChoices.choices))

class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    genre = models.ManyToManyField(Genre)
    publication_date = models.DateField()

    def __str__(self) -> str:
        return self.title


class BookInstance(models.Model):
    class Status(models.TextChoices):
        ON_LOAN = "LN", _("On loan")
        AVAILABLE = "AV", _("Available")
        RESERVED = ""
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    status = models.CharField(choices=Status.choices)
    due_date = models.DateField()



class Borrower(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

class Loan(models.Model):
    book_instance = models.ForeignKey(BookInstance, on_delete=models.DO_NOTHING)
    borrower = models.ForeignKey(Borrower)
    load_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField()
