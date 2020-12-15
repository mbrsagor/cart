from rest_framework.viewsets import ModelViewSet

from .serializers import LibrarySerializer, AuthorSerializer, BookSerializer, InvitationsSerializer, ContactSerializer
from .models import Library, Author, Book, Invitations, Contact


class LibraryViewSet(ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class InvitationsViewSet(ModelViewSet):
	queryset = Invitations.objects.all()
	serializer_class = InvitationsSerializer


class ContactViewSet(ModelViewSet):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer
