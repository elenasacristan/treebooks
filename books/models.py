from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    CATEGORIES_CHOICES = (
        ("Kid's Books", "Kid's Books"),
        ('Politics', 'Politics'),
        ('Self Help', 'Self Help'),
        ('Novel', 'Novel'),
    )
    name = models.CharField(max_length=15, choices=CATEGORIES_CHOICES)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Author(models.Model):
    
    name = models.CharField(max_length=50, default='')
    url_wiki = models.URLField(max_length=250, default='')

    def __str__(self):
        return self.name

class StoreBook(models.Model):
    name = models.CharField(max_length=15)
    street = models.CharField(max_length=15)
    map_store = models.URLField(max_length=400, default='')

    def __str__(self):
        return self.name

class Book(models.Model):
    FORMAT_CHOICES = (
            ('Hardcover', 'Hardcover'),
            ('Paperback', 'Paperback'),
        )
    # STORE_CHOICES = (
    #             ('Store1', 'Store1'),
    #             ('Store2', 'Store2'),
    #         )

    title = models.CharField(max_length=50, default='')

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store = models.ForeignKey(StoreBook, on_delete=models.CASCADE)

    total_number_reviews = models.IntegerField(default=0)
    total_ratings = models.IntegerField(default=0)
    percentage_rating = models.IntegerField(default=0)
    rating = models.DecimalField(decimal_places=2, max_digits=3, default=0.00)
    book_img = models.ImageField(upload_to='images', default="images/book.png")
    ISBN = models.CharField(max_length=25, default='')
    publication_date = models.DateField(default=datetime.now)
    summary = models.TextField()
    format_book = models.CharField(max_length=15, choices=FORMAT_CHOICES)
    price_day = models.DecimalField(decimal_places=2, max_digits=3)
    pages = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    return_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.title



