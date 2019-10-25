from django.test import TestCase
from .forms import ReviewForm

class TestReviewForms(TestCase):

    def test_form_can_be_submitted_with_all_the_fields_filled(self):
        form = ReviewForm({'review_title':'title', 'comment':'random text', 'score':3})
        self.assertTrue(form.is_valid())
    
    def test_form_cannot_be_submitted_without_review_title(self):
        form = ReviewForm({'review_title':'', 'comment':'random text', 'score':3})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['review_title'],[u'This field is required.'])

    def test_form_cannot_be_submitted_without_comment(self):
            form = ReviewForm({'review_title':'title', 'comment':'', 'score':3})
            self.assertFalse(form.is_valid())
            self.assertEqual(form.errors['comment'],[u'This field is required.'])

    def test_form_cannot_be_submitted_without_score(self):
            form = ReviewForm({'review_title':'title', 'comment':'random text', 'score':None})
            self.assertFalse(form.is_valid())
            self.assertEqual(form.errors['score'],[u'This field is required.'])

