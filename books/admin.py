from django.contrib import admin
from .models import Book,Category,Author, StoreBook

# Register your models here.
# we add Book, Category, Author and StoreBook models to the admin site

admin.site.register(Book)

admin.site.register(Category)

admin.site.register(Author)

admin.site.register(StoreBook)

