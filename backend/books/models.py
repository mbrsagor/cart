from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, related_name='auhtor_books')
    title = models.CharField(max_length=100)
    release = models.DateField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE, blank=True, related_name='book_libary')

    def __str__(self):
        return self.title



class Invitations(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email



class Contact(models.Model):
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.email
