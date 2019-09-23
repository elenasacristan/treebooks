from django.db import models

# Create your models here.

class Category(models.Model):
    CATEGORIES_CHOICES = (
        ('B', 'Biography'),
        ('N', 'Novel'),
    )
    name = models.CharField(max_length=1, choices=CATEGORIES_CHOICES)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Book(models.Model):
    FORMAT_CHOICES = (
            ('H', 'Hardcover'),
            ('P', 'Paperback'),
        )
    STORE_CHOICES = (
                ('H', 'Hardcover'),
                ('P', 'Paperback'),
            )

    title = models.CharField(max_length=50, default='')
    views = models.IntegerField(default=0, blank=True,null=True)
    rating = models.DecimalField(decimal_places=2, max_digits=3, blank=True,null=True)
    book_img = models.ImageField(upload_to='images', default="images/book.png")
    ISBN = models.CharField(max_length=17, default='')
    year = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField()
    format_book = models.CharField(max_length=1, choices=FORMAT_CHOICES)
    store = models.CharField(max_length=1, choices=STORE_CHOICES)
    price_day = models.DecimalField(decimal_places=2, max_digits=3)
    pages = models.IntegerField(default=0)
    avg_days = models.IntegerField(default=0)
    language_book = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.title


