from django.shortcuts import get_object_or_404, redirect, render
from books.models import Book, Review
from django.views import generic


class BookListView(generic.ListView):
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


# def index(request):
#     booksData = Book.objects.all()
#     context = {'books': booksData}
#     return render(request, 'books/index.html', context)

class BookDetailView(generic.DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        return context


# def show(request, id):
#     # try:
#     #     singlebook = Book.objects.get(pk=id)
#     # except Book.DoesNotExist:
#     #     raise Http404('Book not found')

#     # to use shortcut findorfail() type
#     singlebook = get_object_or_404(Book, pk=id)
#     reviews = Review.objects.filter(book_id=id).order_by('-created_at')

#     context = {
#         'book': singlebook,
#         'reviews': reviews,
#     }

#     return render(request, 'books/show.html', context)


def review(request, id):
    body = request.POST['review']
    newreview = Review(body=body, book_id=id)
    newreview.save()
    return redirect('/book')


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'books': books}
    return render(request, 'books/book_list.html', context)
