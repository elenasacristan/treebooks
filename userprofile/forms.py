from django import forms
from .models import UserProfile



class UserProfileForm(forms.ModelForm):
    
    profile_img = forms.ImageField(label="<b>Profile Image:</b>")
    dob = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=('%d-%m-%Y', ), label='<b>Date of Birth <small>(dd-mm-yyyy)</small>:</b>')
    telephone = forms.IntegerField(label="<b>Telephone:</b>")
    subscribe = forms.BooleanField(label="Subscribe to our monthly newsletter", required=False)
    contact_by_phone = forms.BooleanField(label="I can be contacted by phone", required=False)
    contact_by_email = forms.BooleanField(label="I can be contacted by email", required=False)

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

