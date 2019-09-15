from django import forms

class LoginForm(forms.Form):
    '''Form to be used to log users in'''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)