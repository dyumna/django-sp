from django.shortcuts import render
from django.http import HttpResponse

from .models import Book

# Create your views here.

def tst(request):
    return HttpResponse('yellow')

def detail(request, book_id):
    book = None
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return HttpResponse(f"Book {book_id} doesn't exist")

    return HttpResponse(f"Book {book_id} is {book}")

