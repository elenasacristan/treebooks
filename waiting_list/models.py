from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from django.utils import timezone

# Create your models here.
class WaitingList(models.Model):
    date_joined = models.DateTimeField(blank=True, null=True, default=timezone.now)
    wl_book = models.OneToOneField(Book, related_name="related_book")
    wl_user = models.ManyToManyField(User, related_name='users')
    
    def __str__(self):
        return "{0} - {1}".format(self.date_joined.strftime('%m/%d/%Y'), self.wl_book)  

    class Meta:
       ordering = ('wl_book','date_joined',)