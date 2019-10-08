from django.shortcuts import render, get_object_or_404
from .models import Book, Category
from reviews.models import ReviewBook
from waiting_list.models import WaitingList

# Create your views here.

def view_all_books(request):
    '''
    This view will display all the books 
    sorted by publication date
    '''
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, 'all_books.html', {'books':books, 'categories':categories})

def detail(request, pk):
    book = get_object_or_404(Book,pk=pk)
    book.save()
    reviews = ReviewBook.objects.filter(reviewed_book__id=pk)
    waiting_list = WaitingList.objects.filter(wl_book__id=pk, wl_user=request.user)

    return render(request, 'detail.html', 
                {'book':book,
                'reviews':reviews,
                'waiting_list':waiting_list})
