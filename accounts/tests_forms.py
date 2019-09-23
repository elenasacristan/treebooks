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

    def test_both_passwords_filled_in(self):
        form = RegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email@test.es', 
            'username':'username', 
            'password1':'', 
            'password2':'wwwww1111'})
        self.assertFalse(form.is_valid())  
        self.assertEqual(form.errors['password2'],[u'Please confirm your password'])

    def test_unique_email_in_registration(self):
        form = RegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email@test.es', 
            'username':'username', 
            'password1':'12345abcds', 
            'password2':'12345abcds'})
        self.assertTrue(form.is_valid())
        
        form.save()
        form2 = RegistrationForm({
            'first_name':'first_name2',
            'last_name':'last_name2', 
            'email':'email@test.es', 
            'username':'username2', 
            'password1':'12345abcds', 
            'password2':'12345abcds'})
        self.assertFalse(form2.is_valid())
        self.assertEqual(form2.errors['email'],[u'Email address must be unique'])

    def test_unique_username_in_registration(self):
        form = RegistrationForm({
            'first_name':'first_name',
            'last_name':'last_name', 
            'email':'email@test.es', 
            'username':'username', 
            'password1':'12345abcds', 
            'password2':'12345abcds'})
        self.assertTrue(form.is_valid())
        
        form.save()
        form2 = RegistrationForm({
            'first_name':'first_name2',
            'last_name':'last_name2', 
            'email':'test@test.es', 
            'username':'username', 
            'password1':'12345abcds', 
            'password2':'12345abcds'})
        self.assertFalse(form2.is_valid())
        self.assertEqual(form2.errors['username'],[u'A user with that username already exists.'])


    # def test_user_cannot_login_without_username(self):
    #     form = LoginForm({'username':'', 'password':'password'})
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors['username'],[u'This field is required.'])

    # def test_user_cannot_login_without_password(self):
    #     form = LoginForm({'username':'username', 'password':''})
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors['password'],[u'This field is required.'])
