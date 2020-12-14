from django.contrib import admin
from .models import Library, Author, Book, Invitations

admin.site.register(Library)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Invitations)