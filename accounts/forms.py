from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    '''Form to be used to log users in'''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    '''Form used to register a new user'''
    password1 = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm the password", 
        widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username', 'password1', 'password2']


    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name


    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return last_name


    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError(u'Please confirm your password')
        
        if password1 != password2:
            raise forms.ValidationError(u'The passwords must match')

        
