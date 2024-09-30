# book_store/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("book_outlet.urls")),  # Correctly map to book_outlet URLs
]
