from django import forms
from .models import UserProfile



class UserProfileForm(forms.ModelForm):
    
    profile_img = forms.ImageField(label="<b>Profile Image:</b>")
    dob = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=('%d-%m-%Y', ), label='<b>Date of Birth:</b>')
    telephone = forms.IntegerField(label="<b>Telephone:</b>")
    subscribe = forms.BooleanField(label="Subscribe to our monthly newsletter")
    contact_by_phone = forms.BooleanField(label="I can be contacted by phone")
    contact_by_email = forms.BooleanField(label="I can be contacted by email")

    class Meta:
        model = UserProfile
        fields = [
            'profile_img',
            'subscribe',
            'dob',
            'telephone',
            'contact_by_phone',
            'contact_by_email'
            ]

