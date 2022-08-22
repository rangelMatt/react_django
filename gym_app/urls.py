from django.urls import path
from . import views

urlpatterns = [
    path('the_gym', views.the_gym),
]