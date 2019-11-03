from django.test import TestCase, Client
from django.contrib.auth.models import User
from userprofile.models import UserProfile 
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm
from books.models import Book, Category, StoreBook, Author

"""
I learn about Client, login, logout, testing redirects in the following link 
https://docs.djangoproject.com/en/1.11/topics/testing/tools/

I learn about setUp in the following link
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
"""

c=Client()

# Create your tests here.
class TestHomeViews(TestCase):

    '''
    the user needs to be authenticated in order to add 
    books to favourites
    '''
    def setUp(self):
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

     
        self.userprofile = UserProfile.objects.create(
            user = self.user,
            subscribe = False,
            dob = '2000-01-01',
            telephone = "",
            contact_by_phone = False,
            contact_by_email = False,
        )
      
    def test_add_and_remove_from_favourites(self):       
        #first_click_add
        response = c.post('/favourites/addremove/{0}'.format(self.book.id))
        self.assertIn(self.book, self.userprofile.favourites.all())

        #second_click_remove
        response = c.post('/favourites/addremove/{0}'.format(self.book.id))
        self.assertNotIn(self.book, self.userprofile.favourites.all())
    
 
    def test_favourites_cannot_be_used_by_not_authenticated_user(self):
        c.logout()      
        page = c.post('/favourites/addremove/{0}'.format(self.book.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/accounts/login/?next=/favourites/addremove/{0}'.format(self.book.id))