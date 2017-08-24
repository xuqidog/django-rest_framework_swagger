from django.shortcuts import render
from restApi.models import Book
from restApi.serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


class BookDetail(APIView):
    def get(self, request, num, format=None):
        b = Book.objects.get(id=num)
        ser = BookSerializer(b)
        return Response(ser.data)


class BookList(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
