from django.shortcuts import get_object_or_404
from books.models import Book


def cart_content(request):
    '''
    We will create a context that will be available to
    all pages
    '''

    '''
    We will request the cart if there is one or a 
    blank dictionary if there is none
    '''
    cart = request.session.get('cart',{})
    cart_books = []
    total = 0
    books_count = 0
    book_price = 0

    for id, days in cart.items():
        book = get_object_or_404(Book, pk=id)
        book_price = days * book.price_day
        total += book_price
        books_count += 1
        cart_books.append({'id':id, 'book_price':book_price, 'days':days, 'book':book})
    
    return {'cart_books':cart_books, 'total':total, 'books_count':books_count}
    


