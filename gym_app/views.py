from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
class Another(View):
    def get(self, request):
        return HttpResponse('This is another function inside class')


def the_gym(request):
    return HttpResponse('First message from views')
