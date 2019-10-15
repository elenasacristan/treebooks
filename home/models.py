from django.db import models
from datetime import datetime

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=250, default='')
    target = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return "{0} - £{1}".format(self.name, self.target)
    
    class Meta:
        verbose_name_plural = "Projects"


class TotalRaised(models.Model):  
    number_books =  models.IntegerField(default=0)
    money_raised = models.DecimalField(max_digits=9, decimal_places=2) 

    class Meta:
        verbose_name_plural = "Total Raised"

    def __str__(self):
        return "£{0} - {1} books".format(self.money_raised, self.number_books)


class ContactUs(models.Model):
    
    email = models.EmailField(max_length=70)
    content = models.TextField()
    contact_date = models.DateField(default=datetime.now)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return "{0} - {1}, {2}".format(self.answered, self.contact_date, self.email)

    class Meta:
        verbose_name_plural = 'contact emails'



def clean_email(self):
            email = self.cleaned_data.get('email')
            
            if not email:
                raise forms.ValidationError(u'This field is required.')
            return email

def clean_content(self):
            content = self.cleaned_data.get('content')
            
            if not content:
                raise forms.ValidationError(u'This field is required.')
            return content

