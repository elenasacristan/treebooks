from django.test import TestCase
from books.models import Book, Author, Category, StoreBook
from .models import Order, OrderLineItem

'''
I learn about setUp in the following link
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
'''

# Create your tests here.
class TestCheckoutModels(TestCase):

    '''set up the category, store and author to use in the tests so we
    don't have to repeat the setup in each test'''
    def setUp(self):
        #create order
        self.order = Order(
            full_name='Name',
            phone_number='11111',
            country='UK',
            postcode='SE11',
            town_or_city = 'London',
            street_address1 = 'street',
            street_address2 = 'street2',
            county = 'London',
            date = 2000-10-10)

        #create book
        test_category = Category.objects.create(name='Novel')
        test_store = StoreBook.objects.create(name='Store name', street='street name', map_store='www.test.com' )
        test_author = Author.objects.create(name='Name author')

        book = Book.objects.create(title="book title", 
        author=test_author,  
        category=test_category,
        total_number_reviews=0,
        total_ratings=0,
        percentage_rating=0,
        rating=0.00,
        ISBN='2313434',
        publication_date='2019-01-01',
        summary='dasdasd dfsdfsdf sdfsdf',
        format_book='Hardcover',
        store=test_store,
        price_day=0.05,           
        pages=200,
        available=False,
        return_date='2019-01-01')

        #create order in line 15 days
        self.order_inline = OrderLineItem(
            order = self.order,
            book = book,
            days = 15
        )  

    def test_can_create_order_with_all_the_fields(self):
        self.assertEqual(self.order.full_name, 'Name')
    
    def test_can_create_order_line_item_with_all_the_fields(self):
        self.assertEqual(self.order_inline.order.full_name, 'Name')
        self.assertEqual(self.order_inline.days, 15)

    



