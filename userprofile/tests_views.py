from django.test import TestCase, Client
from .forms import UserProfileForm
from accounts.forms import RegistrationForm


c=Client()

class TestUserProfileViews(TestCase):

    def test_view_profile_page_not_authenticated_users(self):
        '''Test that the profile is not available
        if the user is not authenticated and if someone
        try to access gets redirected to the login page'''
        page = c.get("/profile/")
        self.assertRedirects(page, '/accounts/login/?next=/profile/')     

           
    def test_view_profile_page_authenticated_users(self):
        '''Test authenticated user get can see the profile page'''
        user = RegistrationForm({"first_name":"first_name", "last_name":"last_name","username":"username", "email":"test@test.com", "password1":"qwer1234", "password2":"qwer1234"})
        user.save()
            
        login_ok = c.login(username="username", password="qwer1234")
        self.assertTrue(login_ok)
        
        page = c.get("/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_profile.html")

    def test_edit_profile_page_not_authenticated_users(self):
        '''Test that the edit_user_profile page is not available
        if the user is not authenticated and if someone
        try to access gets redirected to the login page'''
        page = c.get("/profile/edit/1")
        self.assertRedirects(page, '/accounts/login/?next=/profile/edit/1') 
    
    def test_edit_profile_page_authenticated_users(self):
        '''Test authenticated user get can see the profile page'''
        user = RegistrationForm({"first_name":"first_name", "last_name":"last_name","username":"username", "email":"test@test.com", "password1":"qwer1234", "password2":"qwer1234"})
        user.save()
            
        login_ok = c.login(username="username", password="qwer1234")
        self.assertTrue(login_ok)
        
        page = c.get("/profile/edit/1")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_user_profile.html")


       