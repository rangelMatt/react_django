from rest_framework import viewsets
from gym_app.serializers import BookSerializer
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()