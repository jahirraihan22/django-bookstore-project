from django.shortcuts import render


def index(request):
    context = {'name': 'Jahir'}
    return render(request, 'books/index.html', context)
