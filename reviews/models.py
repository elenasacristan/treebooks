from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from django.utils import timezone
# from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.


class ReviewBook(models.Model):

    CHOICES = [(i,i) for i in range(6)]

    review_title = models.CharField(max_length=35, null=True, blank=True)
    comment = models.TextField()
    score = models.IntegerField(default=0, choices=CHOICES)
    review_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    review_author = models.ForeignKey(User)
    reviewed_book = models.ForeignKey(Book, default='')
    
    def __str__(self):
        return "{0} - {1}, {2}".format(self.score, self.review_title, self.review_author)  