from django.test import TestCase, Client
from .models import Book, Author, Category

c=Client()

# Create your tests here.
class TestBookViews(TestCase):
    
    def test_all_books_page(self):
        page = c.get("/books/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "all_books.html")

    

 