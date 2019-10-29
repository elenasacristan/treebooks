from django.test import TestCase, Client
from books.models import Book, Author, Category, StoreBook
from django.core.files.uploadedfile import SimpleUploadedFile
from base64 import b64decode
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

c=Client()

# Create your tests here.
class TestSearchViews(TestCase):

    def setUp(self):
        test_category = Category.objects.create(name='Novel')
        test_store = StoreBook.objects.create(name='Store name', street='street name', map_store='www.test.com' )
        test_author1 = Author.objects.create(name='Author ONE')
        test_author2 = Author.objects.create(name='all Author TWO')

        self.book1 = Book.objects.create(title="all book title ABC", 
        author=test_author1,  
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

        self.book2 = Book.objects.create(title="book title DEF", 
        author=test_author2,  
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

        self.book3 = Book.objects.create(title="book title", 
        author=test_author2,  
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

    
    def test_search_redirects_to_all_books_page(self):
        page = c.get("/search/?q=ABC")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "all_books.html")

    def test_that_1_books_contain_ABC_in_book_title(self):
        page = c.get("/search/?q=ABC")
        page.context['books']
        self.assertEqual(len(page.context['books']), 1)

    def test_that_3_books_contain_book_in_book_title(self):
        page = c.get("/search/?q=book")
        page.context['books']
        self.assertEqual(len(page.context['books']), 3)

    def test_that_2_books_contain_TWO_in_book_author(self):
        page = c.get("/search/?q=TWO")
        page.context['books']
        self.assertEqual(len(page.context['books']), 2)

    def test_that_3_books_contain_all_in_book_author_or_title(self):
        page = c.get("/search/?q=all")
        page.context['books']
        self.assertEqual(len(page.context['books']), 3)


    






