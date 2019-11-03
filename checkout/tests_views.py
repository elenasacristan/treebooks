from django.test import TestCase, Client
from accounts.forms import RegistrationForm
from books.models import Book, Author, Category, StoreBook

"""
I learn about Client, login, logout, testing redirects in the following link 
https://docs.djangoproject.com/en/1.11/topics/testing/tools/

I learn about setUp in the following link
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
"""
c=Client()

# Create your tests here.
class TestCartViews(TestCase):  

    def setUp(self):
        '''In order to test checkout the user needs to be logged in'''
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

      








