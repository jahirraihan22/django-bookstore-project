from django.shortcuts import render
from books.models import Book


def index(request):
    booksData = Book.objects.all()
    context = {'books': booksData}
    return render(request, 'books/index.html', context)


def show(request, id):
    singlebook = Book.objects.get(pk=id)
    context = {'book': singlebook}
    return render(request, 'books/show.html', context)
