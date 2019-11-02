from django.test import TestCase, Client
from .models import Book, Author, Category, StoreBook

"""
I learn about Client in the following link 
https://docs.djangoproject.com/en/1.11/topics/testing/tools/

I learn about setUp in the following link
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
"""

c=Client()

# Create your tests here.
class TestBookViews(TestCase):


    def setUp(self):
        test_category = Category.objects.create(name='Novel')
        test_store = StoreBook.objects.create(name='Store name', street='street name', map_store='www.test.com' )
        test_author = Author.objects.create(name='Name author')

        self.book = Book.objects.create(title="book title", 
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

    
    def test_all_books_page(self):
        page = c.get("/books/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "all_books.html")


    def test_detail_view(self):
        page = c.get("/books/{0}/".format(self.book.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "detail.html")








