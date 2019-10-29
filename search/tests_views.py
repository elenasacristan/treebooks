# from django.test import TestCase, Client
# from books.models import Book, Author, Category, StoreBook
# from django.core.files.uploadedfile import SimpleUploadedFile
# from base64 import b64decode
# from django.core.files.base import ContentFile
# from django.core.files.uploadedfile import InMemoryUploadedFile
# from io import BytesIO

# c=Client()

# # Create your tests here.
# class TestSearchViews(TestCase):

#     def setUp(self):
#         test_category = Category.objects.create(name='Novel')
#         test_store = StoreBook.objects.create(name='Store name', street='street name', map_store='www.test.com' )
#         test_author1 = Author.objects.create(name='Author ONE')
#         test_author2 = Author.objects.create(name='all Author TWO')


#         #create fake image
#         image_data = b64decode("iVBORw0KGgoAAAANSUhEUgAAAQMAAACwCAIAAACEmpzzAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAKRSURBVHhe7dPBjhRJEAVB/v+nG7n0RmxtgWCgR+quMrtlxjHCvz2Ax0MJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJkPuW8O3D3tzbTe9gEXzYLzemhNmAu1LCD5txS/dd/87/ZGNu5taL3+2fbMyd3H3ru/2TjbkNKxcDse/Z+R9txg1Y9g87/6PNuDqbPtj5H23GpVnz/+38Tzbmoiz4J3b7JxtzRbb7c7v9k425HKv9pd3+ycZci73+xs7/aDMuxFJ/b+d/tBlXYaN/ZOd/tBmXYJ1/aud/tBnvzy4/Yed/sjHvzBY/Z7d/sjFvywo/bbd/sjHvyf7+xm7/ZGPekOX9vZ3/0Wa8G5v7Jzv/o814K9b2r3b+R5vxPuzsCXb+R5vxJizsOXb+Jxvz8qzqaXb7Jxvz2uzpmXb7JxvzwizpyXb7JxvzqmzoS+z8jzbjJVnPV9n5/8cGvCTr+UIr4MN+eUnW87UWgQxeng1BlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAkQJECVAlABRAjwej8d3KdJWtZCwOToAAAAASUVORK5CYII=")
#         image_file = ContentFile(image_data, 'test_image.png')

#         image = InMemoryUploadedFile(
#             BytesIO(image_data),
#             field_name='tempfile',
#             name='test_image.png',
#             content_type='image/png',
#             size=len(image_data),
#             charset='utf-8',
#         )
#         self.in_memory_image = image

#         self.uploaded_image_file = SimpleUploadedFile(
#             image_file.name, 
#             image_file.read(), 
#             content_type="image/png"
#         )

#         self.book1 = Book.objects.create(title="all book title ABC", 
#         author=test_author1,  
#         category=test_category,
#         total_number_reviews=0,
#         total_ratings=0,
#         percentage_rating=0,
#         rating=0.00,
#         book_img=image,
#         ISBN='2313434',
#         publication_date='2019-01-01',
#         summary='dasdasd dfsdfsdf sdfsdf',
#         format_book='Hardcover',
#         store=test_store,
#         price_day=0.05,           
#         pages=200,
#         available=False,
#         return_date='2019-01-01')

#         self.book1 = Book.objects.create(title="book title DEF", 
#         author=test_author2,  
#         category=test_category,
#         total_number_reviews=0,
#         total_ratings=0,
#         percentage_rating=0,
#         rating=0.00,
#         book_img=image,
#         ISBN='2313434',
#         publication_date='2019-01-01',
#         summary='dasdasd dfsdfsdf sdfsdf',
#         format_book='Hardcover',
#         store=test_store,
#         price_day=0.05,           
#         pages=200,
#         available=False,
#         return_date='2019-01-01')

#         self.book1 = Book.objects.create(title="book title", 
#         author=test_author2,  
#         category=test_category,
#         total_number_reviews=0,
#         total_ratings=0,
#         percentage_rating=0,
#         rating=0.00,
#         book_img=image,
#         ISBN='2313434',
#         publication_date='2019-01-01',
#         summary='dasdasd dfsdfsdf sdfsdf',
#         format_book='Hardcover',
#         store=test_store,
#         price_day=0.05,           
#         pages=200,
#         available=False,
#         return_date='2019-01-01')

    
#     def test_search_redirects_to_all_books_page(self):
#         page = c.get("/search/?q=ABC")
#         self.assertEqual(page.status_code, 200)
#         self.assertTemplateUsed(page, "all_books.html")

#     def test_that_1_books_contain_ABC_in_book_title(self):
#         page = c.get("/search/?q=ABC")
#         page.context['books']
#         self.assertEqual(len(page.context['books']), 1)

#     def test_that_3_books_contain_book_in_book_title(self):
#         page = c.get("/search/?q=book")
#         page.context['books']
#         self.assertEqual(len(page.context['books']), 3)

#     def test_that_2_books_contain_TWO_in_book_author(self):
#         page = c.get("/search/?q=TWO")
#         page.context['books']
#         self.assertEqual(len(page.context['books']), 2)

#     def test_that_3_books_contain_all_in_book_author_or_title(self):
#         page = c.get("/search/?q=all")
#         page.context['books']
#         self.assertEqual(len(page.context['books']), 3)


    






