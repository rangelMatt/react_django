from django.urls import path
from . import views
from .views import Another

urlpatterns = [
    path('the_gym', views.the_gym),
    path('another', Another.as_view()),
]