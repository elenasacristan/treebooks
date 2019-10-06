from django import forms
from .models import ReviewBook
from django.core.exceptions import ValidationError


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ReviewBook
        fields = ('review_title', 'comment', 'score')

    def clean_review_title(self):
            review_title = self.cleaned_data.get('review_title')
            
            if not review_title:
                raise forms.ValidationError(u'This field is required.')
            return review_title
    
    def clean_comment(self):
            comment = self.cleaned_data.get('comment')
            
            if not comment:
                raise forms.ValidationError(u'This field is required.')
            return comment

    def clean_score(self):
            score = self.cleaned_data.get('score')
            
            if not score:
                raise forms.ValidationError(u'This field is required.')

            return score