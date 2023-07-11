from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from .models import BookModel,AuthorModel
from rest_framework.response import Response
from .serializers import BookSerializer,AuthorSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsOwnerPermission


class AllBookView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerPermission,)

class DetailBookView(generics.RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerPermission,)

class AllCreateBookView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

class UpdateBookView(generics.UpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

class DetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


