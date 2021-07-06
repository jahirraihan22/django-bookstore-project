from django.shortcuts import render
import json

booksData = open(
    '/home/jahir/Downloads/codes/django/bookstore-project/books.json').read()

data = json.loads(booksData)


def index(request):
    context = {'books': data}
    return render(request, 'books/index.html', context)


def show(request, id):
    singlebook = list()
    for book in data:
        if book['id'] == id:
            singlebook = book
    context = {'book': singlebook}
    return render(request, 'books/show.html', context)
