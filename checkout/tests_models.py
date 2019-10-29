from django.test import TestCase
from books.models import Book, Author, Category, StoreBook
from .models import Order, OrderLineItem
from django.core.files.uploadedfile import SimpleUploadedFile
from base64 import b64decode
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from datetime import datetime

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

        #create fake image
        # image_data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAQMAAACwCAIAAACEmpzzAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAKRSURBVHhe7dPBjhRJEAVB/v+nG7n0RmxtgWCgR+quMrtlxjHCvz2Ax0MJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJkPuW8O3D3tzbTe9gEXzYLzemhNmAu1LCD5txS/dd/87/ZGNu5taL3+2fbMyd3H3ru/2TjbkNKxcDse/Z+R9txg1Y9g87/6PNuDqbPtj5H23GpVnz/+38Tzbmoiz4J3b7JxtzRbb7c7v9k425HKv9pd3+ycZci73+xs7/aDMuxFJ/b+d/tBlXYaN/ZOd/tBmXYJ1/aud/tBnvzy4/Yed/sjHvzBY/Z7d/sjFvywo/bbd/sjHvyf7+xm7/ZGPekOX9vZ3/0Wa8G5v7Jzv/o814K9b2r3b+R5vxPuzsCXb+R5vxJizsOXb+Jxvz8qzqaXb7Jxvz2uzpmXb7JxvzwizpyXb7JxvzqmzoS+z8jzbjJVnPV9n5/8cGvCTr+UIr4MN+eUnW87UWgQxeng1BlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAjwej8d3KdJWtZCwOToAAAAASUVORK5CYII=")
        # image_file = ContentFile(image_data, 'test_image.png')

        # image = InMemoryUploadedFile(
        #     BytesIO(image_data),
        #     field_name='tempfile',
        #     name='test_image.png',
        #     content_type='image/png',
        #     size=len(image_data),
        #     charset='utf-8',
        # )
        # self.in_memory_image = image

        # self.uploaded_image_file = SimpleUploadedFile(
        #     image_file.name, 
        #     image_file.read(), 
        #     content_type="image/png"
        # )

        book = Book.objects.create(title="book title", 
        author=test_author,  
        category=test_category,
        total_number_reviews=0,
        total_ratings=0,
        percentage_rating=0,
        rating=0.00,
        # book_img=image,
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

    



