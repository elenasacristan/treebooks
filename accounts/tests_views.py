from django.test import TestCase, Client
from accounts.forms import RegistrationForm

c=Client()

# Create your tests here.
class TestAccountsViews(TestCase):
    
    def test_login_page(self):
        page = c.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")


    def test_registration_page(self):
        page = c.get("/accounts/registration/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
        

    def test_login_functionality_user_registered(self):
        user = RegistrationForm({"first_name":"first_name", "last_name":"last_name","username":"username", "email":"test@test.com", "password1":"qwer1234", "password2":"qwer1234"})
        user.save()
            
        login_ok = c.login(username="username", password="qwer1234")
        self.assertTrue(login_ok)
   

    def test_login_functionality_user_not_registered(self):
        user = RegistrationForm({"first_name":"first_name", "last_name":"last_name","username":"username", "email":"test@test.com", "password1":"qwer1234", "password2":"qwer1234"})
        user.save()
            
        login_ok = c.login(username="otherusername", password="qwer1234")
        self.assertFalse(login_ok)

    def test_logout_functionality(self):
        user = RegistrationForm({"first_name":"first_name", "last_name":"last_name","username":"username", "email":"test@test.com", "password1":"qwer1234", "password2":"qwer1234"})
        user.save()
            
        login_ok = c.login(username="username", password="qwer1234")
        self.assertTrue(login_ok)
        
        page = c.get("/accounts/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/')

    
    def test_user_cant_log_out_when_already_loged_out(self):
        user = RegistrationForm({"first_name":"first_name", "last_name":"last_name","username":"username", "email":"test@test.com", "password1":"qwer1234", "password2":"qwer1234"})
        user.save()
            
        login_ok = c.login(username="username", password="qwer1234")
        self.assertTrue(login_ok)
        
        page = c.logout()      

        page = c.get("/accounts/logout/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/accounts/login/?next=/accounts/logout/')

    def test_authenticated_user_redirected_to_index_if_tries_to_log_in_again(self):
        user = RegistrationForm({"first_name":"first_name", "last_name":"last_name","username":"username", "email":"test@test.com", "password1":"qwer1234", "password2":"qwer1234"})
        user.save()
            
        login_ok = c.login(username="username", password="qwer1234")
        self.assertTrue(login_ok)
        
        page = c.get("/accounts/login/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertRedirects(page, '/')
    
    
    