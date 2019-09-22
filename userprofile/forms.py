from django import forms
from .models import UserProfile
from dobwidget import DateOfBirthWidget


# class UserProfileForm(forms.ModelForm):

#     class Meta:
#         dob = forms.DateField(
#             required=False, 
#             input_formats= ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'])
#         model = UserProfile
#         fields = ['profile_img','subscribe','bio','dob','telephone']

# YEARS= [x for x in range(1940,2021)]


# class UserProfileForm(forms.ModelForm):

#     class Meta:
#         model = UserProfile
#         dob = forms.DateField(
#             label='What is your birth date?', 
#             widget=forms.SelectDateWidget(years=YEARS))

#         fields = ['profile_img','subscribe','bio','dob','telephone']



class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['profile_img','subscribe','bio','dob','telephone']
        widgets = {
            'dob': DateOfBirthWidget(),
        }
        