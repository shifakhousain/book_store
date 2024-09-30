# book_outlet/views.py
from django.shortcuts import render

def index(request):
    return render(request, "book_outlet/index.html")
