from django.test import TestCase
from .forms import ContactUsForm

class TestHomeForms(TestCase):

    def test_form_can_be_submitted_with_all_the_fields_filled(self):
        form = ContactUsForm({'email':'email@email.com', 'content':'random text'})
        self.assertTrue(form.is_valid())
    
    def test_form_cannot_be_submitted_without_email(self):
        form = ContactUsForm({'email':'', 'content':'random text'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],[u'This field is required.'])

    def test_form_cannot_be_submitted_without_content(self):
        form = ContactUsForm({'email':'email@email.com', 'content':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'],[u'This field is required.'])

    def test_email_field_needs_to_have_email_format(self):
        form = ContactUsForm({'email':'emailemail.com', 'content':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],[u'Enter a valid email address.'])
