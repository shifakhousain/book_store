# book_outlet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("<str:title>", views. book_detail, name="book_detail"),
]