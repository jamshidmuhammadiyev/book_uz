from rest_framework import serializers
from .models import BookModel, AuthorModel, BookCategoryModel
from django.shortcuts import get_object_or_404


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('name', 'f_name', 'date_of_birth', 'country')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id', 'author', 'name', 'category', 'page', 'price')