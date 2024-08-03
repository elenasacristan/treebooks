from django.urls import path
from .views import view_all_books, detail, return_book


urlpatterns = [
    path('', view_all_books, name='view_all_books'),
    path('<int:pk>/', detail, name='detail'),
    path('return/<int:pk>/', return_book, name='return_book'),
]

