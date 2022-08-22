from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


# Create your views here.
class Another(View):

    book = Book.objects.get(id=1)
    output = f"We have {book.title} book with ID {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)


def the_gym(request):
    return HttpResponse('First message from views')
