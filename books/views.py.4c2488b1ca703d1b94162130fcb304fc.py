from django.shortcuts import render, get_object_or_404
from .models import Book, Category

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
    book.views += 1
    book.save()
    return render(request, 'detail.html', {'book':book})
