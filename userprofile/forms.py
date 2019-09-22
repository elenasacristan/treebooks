from django import forms
from .models import UserProfile
from dobwidget import DateOfBirthWidget


class UserProfileForm(forms.ModelForm):
    
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
        widgets = {
            'dob': DateOfBirthWidget(),
        }
        