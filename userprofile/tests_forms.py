from django.test import TestCase
from .models import UserProfile
from .forms import UserProfileForm

"""
I learn about setUp in the following link
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
"""

class TestUserProfileForm(TestCase):

    def setUp(self):
        self.profile_form = UserProfileForm({
            'profile_img' : None,
            'subscribe' : False,
            'dob' : '01-01-2000',
            'telephone' : '4435453',
            'contact_by_phone' : False,
            'contact_by_email' : False
        })


    def test_correct_label_in_date_field(self): 
        self.assertTrue(self.profile_form.fields['dob'].label == '<b>Date of Birth <small>(dd-mm-yyyy)</small>:</b>')
        
    def test_correct_format_in_date_field(self):
        self.assertEqual(self.profile_form.fields['dob'].input_formats, ('%d-%m-%Y', ))
    
    def test_correct_label_in_telephone_field(self): 
        self.assertTrue(self.profile_form.fields['telephone'].label == "<b>Telephone:</b>")

    def test_correct_label_in_subscribe_field(self): 
        self.assertTrue(self.profile_form.fields['subscribe'].label == "Subscribe to our monthly newsletter")
 
    def test_correct_label_in_contact_by_phone_field(self): 
        self.assertTrue(self.profile_form.fields['contact_by_phone'].label == "I can be contacted by phone")

    def test_correct_label_in_contact_by_email_field(self): 
        self.assertTrue(self.profile_form.fields['contact_by_email'].label == "I can be contacted by email")
