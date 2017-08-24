from __future__ import unicode_literals
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)