from django.test import TestCase
from .models import WaitingList
from django.contrib.auth.models import User
from books.models import Book, Category, StoreBook, Author

"""
I learn about setUp in the following link
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
"""

# Create your tests here.
class TestWaitingListModels(TestCase):

    def setUp(self):
        
        self.user = User.objects.create(username="username", password="password1234")
        self.user2 = User.objects.create(username="username2", password="password1234")
    
        test_category = Category.objects.create(name='Novel')
        test_store = StoreBook.objects.create(name='Store name', street='street name', map_store='www.test.com' )
        test_author = Author.objects.create(name='Name author')

        self.book = Book.objects.create(
        title="book title", 
        author=test_author,  
        category=test_category,
        total_number_reviews=0,
        total_ratings=0,
        percentage_rating=0,
        rating=0.00,
        ISBN='2313434',
        publication_date='2019-01-01',
        summary='dasdasd dfsdfsdf sdfsdf',
        format_book='Hardcover',
        store=test_store,
        price_day=0.05,           
        pages=200,
        available=False,
        return_date='2019-01-01') 


    def test_can_create_review(self):
        waitinglist = WaitingList(wl_book = self.book)
        waitinglist.save()
        waitinglist.wl_user.add(self.user)
        waitinglist.wl_user.add(self.user2)

        self.assertEqual(waitinglist.wl_book.title, 'book title')
        
        
