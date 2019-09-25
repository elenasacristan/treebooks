from django.shortcuts import render
from books.models import Book
from django.db.models import Q

# Create your views here.

def do_search(request):
      
    books = Book.objects.filter(Q(title__icontains = request.GET['search']) | Q(author__name__icontains = request.GET['search']))
    return render(request, 'all_books.html', {'books':books})
    