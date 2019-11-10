from django.shortcuts import render, get_object_or_404
from .models import Book, Category
from reviews.models import ReviewBook
from waiting_list.models import WaitingList
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.utils import timezone


# Create your views here.

def view_all_books(request):
    '''
    This view will display all the books sorted by rating descending
    '''
    if request.user.is_authenticated:
        user_profile = User.objects.get(email=request.user.email)
        # list of books ids that the user is currently reading
        current_books_list = list(user_profile.profile.current_books.filter(
            return_date__gt = timezone.now(), available = False).values_list('id',  flat=True))
    else:
        current_books_list = []
    
    books = Book.objects.all().order_by('-rating')
    categories = Category.objects.all()
    
    waiting_list = WaitingList.objects.all()
    # this code will give us a list of the book ids that have waiting list
    waiting_list_books = list(WaitingList.objects.all().values_list('wl_book__id',  flat=True))
        
    return render(request, 'all_books.html', {
        'books':books, 
        'categories':categories, 
        'waiting_list':waiting_list, 
        'waiting_list_books':waiting_list_books,
        'current_books_list':current_books_list
        })


def detail(request, pk):
    '''
    This view will display the book details and the 
    reviews for that book sorted by review date descending
    '''
    if request.user.is_authenticated:
        user_profile = User.objects.get(email=request.user.email)
        # list of books that the user is currently reading
        current_books_list = list(user_profile.profile.current_books.filter(
            return_date__gt = timezone.now(), available = False).values_list('id',  flat=True))
    else:
        current_books_list = []

    book = get_object_or_404(Book,pk=pk)
    book.save()
    
    # The reviews will be sorted by date descending. Most recent at the top
    reviews = ReviewBook.objects.filter(reviewed_book__id=pk).order_by('-review_date')
    
    # this code will give us a list of users in the waiting list for that book
    users_in_list_1 = list( WaitingList.objects.filter(wl_book__id=pk).values_list('wl_user__id',  flat=True))
    # remove None records https://www.geeksforgeeks.org/python-remove-none-values-from-list/
    users_in_list = list(filter(None, users_in_list_1)) 
    
    return render(request, 'detail.html', 
                {'book':book,
                'reviews':reviews,
                'users_in_list':users_in_list,
                'current_books_list':current_books_list})


'''
@login_required so only authenticated user can return a book
'''    
@login_required
def return_book(request, pk):
    book = get_object_or_404(Book,pk=pk)
    profile = UserProfile.objects.get(user = request.user)

    if request.method == 'POST':
        # book status will be available
        book.available=True
        book.save()
        # the book will be removed from the current_boos list
        profile.current_books.remove(book)
        profile.save()

    
    # I learned how to redirect to the current page in the following post
    # https://stackoverflow.com/questions/12758786/redirect-return-to-same-previous-page-in-django/12758859
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
