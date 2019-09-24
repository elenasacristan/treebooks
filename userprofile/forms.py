from django import forms
from .models import UserProfile



class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(input_formats=['%d-%m-%Y'], label="Date of Birth (DD-MM-YYYY)")
    class Meta:
        model = UserProfile
        fields = [
            'profile_img',
            'subscribe',
            'bio',
            'dob',
            'telephone',
            'contact_by_phone',
            'contact_by_email'
            ]

