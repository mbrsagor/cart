from rest_framework import serializers

from .models import Library, Author, Book, Invitations


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('id', 'name', 'address','phone')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id','name', 'book')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'release_year', 'Library')


class InvitationsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Invitations
		fields = ('id', 'email')
