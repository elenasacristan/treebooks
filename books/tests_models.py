from django.test import TestCase
from .models import Book, Author, Category, StoreBook
from django.core.files.uploadedfile import SimpleUploadedFile
from base64 import b64decode
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

# Create your tests here.
class TestBookModels(TestCase):

    '''set up the category, store and author to use in the tests so we
    don't have to repeat the setup in each test'''
    def setUp(self):
        self.category = Category(name='Novel')
        self.store = StoreBook(name='Store name', street='street name', map_store='www.test.com' )
        self.author = Author(name='Name author')

    def test_can_create_category_with_name(self):
        self.assertEqual(self.category.name, 'Novel')
        self.assertEqual("Novel", str(self.category))

    
    def test_can_create_store_filling_all_fields(self):
        self.assertEqual(self.store.name, 'Store name')
        self.assertEqual("Store name", str(self.store))


    def test_can_create_author_with_name(self):
        self.assertEqual(self.author.name, 'Name author')
        self.assertEqual("Name author", str(self.author))


    def test_can_create_book(self):
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

        book = Book(title="book title", 
        author=self.author,  
        category=self.category,
        total_number_reviews=0,
        total_ratings=0,
        percentage_rating=0,
        rating=0.00,
        # book_img=image,
        ISBN='2313434',
        publication_date='2019-01-01',
        summary='dasdasd dfsdfsdf sdfsdf',
        format_book='Hardcover',
        store=self.store,
        price_day=0.05,           
        pages=200,
        available=True,
        return_date='2019-01-01')
        
        self.assertEqual(book.title, 'book title')
        self.assertEqual("book title", str(book))




