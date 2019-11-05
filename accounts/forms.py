from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    '''Form used to log users in'''
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'username or email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}))


class RegistrationForm(UserCreationForm):
    '''Form used to register a new user'''
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'first_name'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'last_name'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password1 = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput(
            attrs={'placeholder': 'password'}))
    password2 = forms.CharField(
        label="Confirm the password", 
        widget=forms.PasswordInput(
            attrs={'placeholder': 'confirm password'}))


    '''fields that will be displayed in the form'''
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username', 'password1', 'password2']


    '''validation of first_name'''
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if not first_name:
            raise forms.ValidationError(u'This field is required.')
        return first_name


    '''validation of last_name'''
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        
        if not last_name:
            raise forms.ValidationError(u'This field is required.')
        return last_name


    '''validation of username'''
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username


    '''validation of email'''
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if not email:
            raise forms.ValidationError(u'This field is required.')

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        
        return email
    

    '''validation of passwords'''
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError(u'Please confirm your password')
        
        if password1 != password2:
            raise forms.ValidationError(u'The passwords must match')

        
