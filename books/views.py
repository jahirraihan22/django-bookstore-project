from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from books.models import Book, Review
from django.core.files.storage import FileSystemStorage
from books.form import ReviewForm
# from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(ListView):
    def get_queryset(self):
        return Book.objects.all()


# def index(request):
#     booksData = Book.objects.all()
#     context = {'books': booksData}
#     return render(request, 'books/index.html', context)

class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        context['form'] = ReviewForm()
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
    if request.user.is_authenticated:
        # body = request.POST['body']
        # newReview = Review(body=body, book_id=id,
        #                    user=request.user)

        # if len(request.FILES) != 0:
        #     image = request.FILES['image']
        #     fs = FileSystemStorage()
        #     name = fs.save(image.name, image)
        #     newReview.image = fs.url(name)
        # newReview.save()

        newReview = Review(book_id=id,
                           user=request.user)
        form = ReviewForm(request.POST, request.FILES, instance=newReview)

        if form.is_valid():
            form.save()
        else:
            print('Invalid request')
    return redirect(f'/book/{id}')


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)
