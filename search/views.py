from django.shortcuts import render
from books.models import Book, Category
from django.db.models import Q

'''
I learn about the Q object in the following link
https://docs.djangoproject.com/en/2.2/topics/db/queries/#complex-lookups-with-q-objects
'''

# Create your views here.

def do_search(request):
    '''
    it will find books that contain the words entered in the input box either
    in the book title or in the authors name and the it will display the
    books found ordered by rating descending
    '''
    categories = Category.objects.filter(Q(book__title__icontains = request.GET['q']) | Q(book__author__name__icontains = request.GET['q'])).distinct()
    books = Book.objects.filter(Q(title__icontains = request.GET['q']) | Q(author__name__icontains = request.GET['q'])).order_by('-rating')
    return render(request, 'all_books.html', {'books':books, 'categories':categories})
    