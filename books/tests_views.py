from django.test import TestCase, Client
from .models import Book, Author, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from base64 import b64decode
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

c=Client()

# Create your tests here.
class TestBookViews(TestCase):
    
    def test_all_books_page(self):
        page = c.get("/books/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "all_books.html")

    # def test_detail_view(self):

    #     image_data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAQMAAACwCAIAAACEmpzzAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAKRSURBVHhe7dPBjhRJEAVB/v+nG7n0RmxtgWCgR+quMrtlxjHCvz2Ax0MJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJkPuW8O3D3tzbTe9gEXzYLzemhNmAu1LCD5txS/dd/87/ZGNu5taL3+2fbMyd3H3ru/2TjbkNKxcDse/Z+R9txg1Y9g87/6PNuDqbPtj5H23GpVnz/+38Tzbmoiz4J3b7JxtzRbb7c7v9k425HKv9pd3+ycZci73+xs7/aDMuxFJ/b+d/tBlXYaN/ZOd/tBmXYJ1/aud/tBnvzy4/Yed/sjHvzBY/Z7d/sjFvywo/bbd/sjHvyf7+xm7/ZGPekOX9vZ3/0Wa8G5v7Jzv/o814K9b2r3b+R5vxPuzsCXb+R5vxJizsOXb+Jxvz8qzqaXb7Jxvz2uzpmXb7JxvzwizpyXb7JxvzqmzoS+z8jzbjJVnPV9n5/8cGvCTr+UIr4MN+eUnW87UWgQxeng1BlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAjwej8d3KdJWtZCwOToAAAAASUVORK5CYII=")
    #     image_file = ContentFile(image_data, 'test_image.png')

    #     image = InMemoryUploadedFile(
    #         BytesIO(image_data),
    #         field_name='tempfile',
    #         name='test_image.png',
    #         content_type='image/png',
    #         size=len(image_data),
    #         charset='utf-8',
    #     )
    #     self.in_memory_image = image

    #     self.uploaded_image_file = SimpleUploadedFile(
    #         image_file.name, 
    #         image_file.read(), 
    #         content_type="image/png"
    #     )

    #     book = Book({
    #         'id':1,
    #         'author' : 'Author',
    #         'category' : 'N',
    #         'views' : 1,
    #         'rating' : 3.02,
    #         'book_img' : image,
    #         'ISBN' : 2313434,
    #         'publication_date' : '2019-01-01',
    #         'summary' : 'dasdasd dfsdfsdf sdfsdf',
    #         'format_book' : 'P',
    #         'store' : '1',
    #         'price_day' : 0.05,           
    #         'pages' : 200,
    #         'avg_days' : 15,
    #         'language_book' : 'English',
    #         'available' : True,
    #         'current_reader' : 'elena',
    #         })
        
    #     book.save()
            


    #     page = c.get("/books/1")
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "detail.html")

    

 