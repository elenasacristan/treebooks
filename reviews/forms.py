from django import forms
from .models import ReviewBook
from django.core.exceptions import ValidationError


class ReviewForm(forms.ModelForm):

    review_title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Review title'}))
    comment = forms.CharField( 
        widget=forms.Textarea(attrs={'placeholder': 'Leave your review in this box'}))

    class Meta:
        model = ReviewBook
        fields = ('review_title', 'comment', 'score')

    # review_title validation
    def clean_review_title(self):
            review_title = self.cleaned_data.get('review_title')
            
            if not review_title:
                raise forms.ValidationError(u'This field is required.')
            return review_title

    # comment validation
    def clean_comment(self):
            comment = self.cleaned_data.get('comment')
            
            if not comment:
                raise forms.ValidationError(u'This field is required.')
            return comment

    # score validation
    def clean_score(self):
            score = self.cleaned_data.get('score')
            
            if (score not in [0,1,2,3,4,5]):
                raise forms.ValidationError(u'This field is required.')
            return score