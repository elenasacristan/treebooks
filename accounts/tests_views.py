from django.test import TestCase, Client
from accounts.forms import RegistrationForm

"""
I learn about Client, login, logout, testing redirects in the following link 
https://docs.djangoproject.com/en/1.11/topics/testing/tools/

I learn about setUp in the following link
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
"""

c=Client()

# Create your tests here.
class TestAccountsViews(TestCase):


     '''I set up the registration form to use in the tests so we
    don't have to repeat this setup in each test'''
    def setUp(self):
        self.registration_form = RegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email@test.es', 
            'username':'username', 
            'password1':'12345abcds', 
            'password2':'12345abcds'})


    def test_home_page(self):
        page = c.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    

    def test_login_page(self):
        page = c.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")


    def test_registration_page(self):
        page = c.get("/accounts/registration/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
        

    def test_login_functionality_when_user_is_registered(self):
        self.registration_form.save()  
        
        login_ok = c.login(username="username", password="12345abcds")
        self.assertTrue(login_ok)
   

    def test_user_cannot_login_if_not_registered(self):
        self.registration_form.save()
            
        login_ok = c.login(username="otherusername", password="12345abcds")
        self.assertFalse(login_ok)


    def test_logout_functionality(self):
        self.registration_form.save()
            
        login_ok = c.login(username="username", password="12345abcds")
        self.assertTrue(login_ok)
        
        page = c.get("/accounts/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/')

    
    def test_user_cannot_log_out_when_already_loged_out(self):
        self.registration_form.save()
            
        login_ok = c.login(username="username", password="12345abcds")
        self.assertTrue(login_ok)
        
        page = c.logout()      

        page = c.get("/accounts/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/accounts/login/?next=/accounts/logout/')


    def test_authenticated_user_redirected_to_index_if_tries_to_log_in_again(self):
        self.registration_form.save()
            
        login_ok = c.login(username="username", password="12345abcds")
        self.assertTrue(login_ok)
        
        page = c.get("/accounts/login/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/')
    

    def test_user_can_login_using_email(self):
        self.registration_form.save()
            
        login_ok = c.login(username="email@test.es", password="12345abcds")
        self.assertTrue(login_ok)
        
       
    