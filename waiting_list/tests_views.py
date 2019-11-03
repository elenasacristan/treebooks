from django.test import TestCase, Client
from .models import WaitingList
from books.models import Book, Author, Category, StoreBook
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm

"""
I learn about Client, login, logout, testing redirects in the following link 
https://docs.djangoproject.com/en/1.11/topics/testing/tools/

I learn about setUp in the following link
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
"""

c=Client()

# Create your tests here.
class TestWaitingListsViews(TestCase):

    def setUp(self):
        '''In order to see the waiting list the user needs to be logged in'''
        self.registration_form = RegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email@test.es', 
            'username':'username', 
            'password1':'12345abcds', 
            'password2':'12345abcds'})  
        self.registration_form.save()   
        login_ok = c.login(username="username", password="12345abcds")

        self.user = User.objects.get(username="username")
        
        test_category = Category.objects.create(name='Novel')
        test_store = StoreBook.objects.create(name='Store name', street='street name', map_store='www.test.com' )
        test_author = Author.objects.create(name='Author')

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

        self.waitinglist = WaitingList.objects.create(
            wl_book = self.book
        )
        self.waitinglist.save()
        self.waitinglist.wl_user.add(self.user)      
    
  
    def test_view_waiting_list(self):
        page = c.get("/waiting_list/{0}/".format(self.waitinglist.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "waiting_list.html")


    def test_that_2_users_are_in_the_list(self):
        page = c.logout()  
        registration_form = RegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email2@test.es', 
            'username':'username2', 
            'password1':'12345abcds', 
            'password2':'12345abcds'})  
        registration_form.save()   
        login_ok = c.login(username="username2", password="12345abcds")
        user2 = User.objects.get(username="username2")
        self.waitinglist.wl_user.add(user2)
        page = c.get("/waiting_list/{0}/".format(self.waitinglist.id))        
        self.assertEqual(self.waitinglist.wl_user.count(),2)



    
    

    

    






