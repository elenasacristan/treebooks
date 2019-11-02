from django.test import TestCase
from .models import Book, Author, Category, StoreBook

'''
I learn about setUp in the following link
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
'''

# Create your tests here.
class TestBookModels(TestCase):

    '''
    set up the category, store and author to use in the tests so we
    don't have to repeat that setup in each test
    '''
    def setUp(self):
        self.category = Category(name='Novel')
        self.store = StoreBook(name='Store name', street='street name', map_store='www.test.com' )
        self.author = Author(name='Name author')


    def test_can_create_category_with_name(self):
        self.assertEqual(self.category.name, 'Novel')
        self.assertEqual("Novel", str(self.category))

    
    def test_can_create_store_filling_all_fields(self):
        self.assertEqual(self.store.name, 'Store name')
        self.assertEqual("Store name", str(self.store))


    def test_can_create_author_with_name(self):
        self.assertEqual(self.author.name, 'Name author')
        self.assertEqual("Name author", str(self.author))


    def test_can_create_book(self):
        
        book = Book(title="book title", 
        author=self.author,  
        category=self.category,
        total_number_reviews=0,
        total_ratings=0,
        percentage_rating=0,
        rating=0.00,
        ISBN='2313434',
        publication_date='2019-01-01',
        summary='dasdasd dfsdfsdf sdfsdf',
        format_book='Hardcover',
        store=self.store,
        price_day=0.05,           
        pages=200,
        available=True,
        return_date='2019-01-01')
        
        self.assertEqual(book.title, 'book title')
        self.assertEqual("book title", str(book))




