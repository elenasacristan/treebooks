from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    '''Form used for users to contact the charity'''
    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'email'}))

    content = forms.CharField( widget=forms.Textarea(attrs={'placeholder': 'Use this box to tell us about other reforestation projects or any other comments or questions'}))
    
    class Meta:
        model = ContactUs
        fields = ['email', 'content']
