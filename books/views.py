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
    waiting_list = WaitingList.objects.all()
    waiting_list_books = list(WaitingList.objects.all().values_list('wl_book__id',  flat=True))

    return render(request, 'all_books.html', {'books':books, 'categories':categories, 'waiting_list':waiting_list, 'waiting_list_books':waiting_list_books})


def detail(request, pk):
    book = get_object_or_404(Book,pk=pk)
    book.save()
    
    reviews = ReviewBook.objects.filter(reviewed_book__id=pk).order_by('-review_date')
    
    users_in_list = list( WaitingList.objects.filter( wl_book__id=pk).values_list('wl_user__id',  flat=True))
    count_users= len(users_in_list)
    
    return render(request, 'detail.html', 
                {'book':book,
                'reviews':reviews,
                'users_in_list':users_in_list,
                'count_users':count_users})

def return_book(request, pk):
    book = get_object_or_404(Book,pk=pk)

    if request.method == 'POST':
        book.available=True
        book.save()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
