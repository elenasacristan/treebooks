from django.test import TestCase
from .forms import LoginForm,RegistrationForm

class TestAccountsForms(TestCase):

    def test_user_can_login_with_username_and_password(self):
        form = LoginForm({'username':'username', 'password':'password'})
        self.assertTrue(form.is_valid())

    def test_user_cannot_login_without_username(self):
        form = LoginForm({'username':'', 'password':'password'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'],[u'This field is required.'])

    def test_user_cannot_login_without_password(self):
        form = LoginForm({'username':'username', 'password':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'],[u'This field is required.'])


    def test_user_can_register_filling_all_the_fields(self):
        form = RegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email@test.es', 
            'username':'username', 
            'password1':'12345abcds', 
            'password2':'12345abcds'})
        self.assertTrue(form.is_valid())

    def test_user_cannot_register_without_filling_out_all_fields(self):
        form = RegistrationForm({
            'first_name':'',
            'last_name':'', 
            'email':'', 
            'username':'', 
            'password1':'', 
            'password2':''})
        self.assertFalse(form.is_valid())  
        self.assertEqual(form.errors['first_name'],[u'This field is required.'])
        self.assertEqual(form.errors['last_name'],[u'This field is required.'])
        self.assertEqual(form.errors['email'],[u'This field is required.'])
        self.assertEqual(form.errors['username'],[u'This field is required.'])
        self.assertEqual(form.errors['password1'],[u'This field is required.'])
        self.assertEqual(form.errors['password2'],[u'This field is required.'])
    
    def test_password_dont_match(self):
        form = RegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email@test.es', 
            'username':'username', 
            'password1':'12345abcds', 
            'password2':'wwwww1111'})
        self.assertFalse(form.is_valid())  
        self.assertEqual(form.errors['password2'],[u'The passwords must match'])


    # def test_user_cannot_login_without_username(self):
    #     form = LoginForm({'username':'', 'password':'password'})
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors['username'],[u'This field is required.'])

    # def test_user_cannot_login_without_password(self):
    #     form = LoginForm({'username':'username', 'password':''})
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors['password'],[u'This field is required.'])
