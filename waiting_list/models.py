from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from django.utils import timezone

# Create your models here.
class WaitingList(models.Model):
    wl_book = models.OneToOneField(Book, related_name="related_book", on_delete=models.CASCADE)
    wl_user = models.ManyToManyField(User, related_name='users')
    
    def __str__(self):
        return self.wl_book.title  
