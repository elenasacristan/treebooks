from django.shortcuts import render
from books.models import Book, Category
from django.db.models import Q

# Create your views here.

def do_search(request):
    categories = Category.objects.filter(Q(book__title__icontains = request.GET['q']) | Q(book__author__name__icontains = request.GET['q'])).distinct()
    books = Book.objects.filter(Q(title__icontains = request.GET['q']) | Q(author__name__icontains = request.GET['q']))
    return render(request, 'all_books.html', {'books':books, 'categories':categories})
    