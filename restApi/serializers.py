from restApi.models import Book
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'title', 'author')
#
# class BookSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Book
#         fields = ('name', 'title', 'author', 'url')