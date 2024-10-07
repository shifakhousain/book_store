from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {"books": books})


def book_detail(request,title):
    book = Book.objects.get(title=title)
    return render(request, "book_outlet/book_detail.html",{
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling" : book.is_bestselling

    })
