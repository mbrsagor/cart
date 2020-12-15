from rest_framework import serializers

from .models import Library, Author, Book, Invitations, Contact


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('id', 'name', 'address','phone')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id','name')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'release', 'library')


class InvitationsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Invitations
		fields = ('id', 'email')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('email', 'message')