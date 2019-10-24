from django.test import TestCase, Client
from accounts.forms import RegistrationForm
from books.models import Book, Author, Category, StoreBook
from django.core.files.uploadedfile import SimpleUploadedFile
from base64 import b64decode
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

c=Client()

# Create your tests here.
class TestCartViews(TestCase):    
    def setUp(self):
        '''In order to test the cart the user needs to be logged in'''
        self.registration_form = RegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email@test.es', 
            'username':'username', 
            'password1':'12345abcds', 
            'password2':'12345abcds'})  
        self.registration_form.save()   
        login_ok = c.login(username="username", password="12345abcds")

    def test_cart_page_authenticated_user(self):
        page = c.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")

    def test_cart_cannot_be_access_by_not_authenticated_user(self):
        page = c.logout()      
        page = c.get("/checkout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/accounts/login/?next=/checkout/')

      








