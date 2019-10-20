from django.db import models
from books.models import Book

# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0} - {1}-{2}".format(self.id, self.date.strftime('%m/%d/%Y'), self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False,, null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, null=False, null=True, on_delete=models.SET_NULL)
    days = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.days, self.book.title, self.book.price_day)