from django.shortcuts import render, get_object_or_404
from .models import Book, Category
from reviews.models import ReviewBook
from waiting_list.models import WaitingList
from django.http import HttpResponseRedirect


# Create your views here.

def view_all_books(request):
    '''
    This view will display all the books 
    sorted by publication date
    '''
    books = Book.objects.all().order_by('-rating')
    categories = Category.objects.all()
    waiting_list = WaitingList.objects.all().order_by('date_joined')
    return render(request, 'all_books.html', {'books':books, 'categories':categories, 'waiting_list':waiting_list})


def detail(request, pk):
    book = get_object_or_404(Book,pk=pk)
    book.save()
    reviews = ReviewBook.objects.filter(reviewed_book__id=pk).order_by('-review_date')
    if request.user.is_authenticated:
        waiting_list = WaitingList.objects.filter(wl_book__id=pk, wl_user=request.user)
    else:
        waiting_list = WaitingList()
    waiting_list_users = WaitingList.objects.filter(wl_book__id=pk).order_by('date_joined')

    return render(request, 'detail.html', 
                {'book':book,
                'reviews':reviews,
                'waiting_list':waiting_list,
                'waiting_list_users':waiting_list_users})

def return_book(request, pk):
    book = get_object_or_404(Book,pk=pk)

    if request.method == 'POST':
        book.available=True
        book.save()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
