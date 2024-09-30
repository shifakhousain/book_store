# book_outlet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Use an empty string for the root URL of this app
]
