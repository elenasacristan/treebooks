from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from books.models import Book
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

'''
if the book is already saved as favourite then remove it from favourites.
If the book is not saved as favourite then save it as favourite
'''

'''
@login_required so only authenticated users can have favourites list of books
'''    
@login_required
def add_remove_favourites(request, id):
    book = get_object_or_404(Book,pk=id)

    if request.method == 'POST':
        profile = UserProfile.objects.get(user = request.user)
        fav_book = Book.objects.get(pk=id)
        
        if fav_book in profile.favourites.all():
            profile.favourites.remove(fav_book)
        else:
            profile.favourites.add(fav_book)

    # I learned who to redirect to the current page in the following post
    # https://stackoverflow.com/questions/12758786/redirect-return-to-same-previous-page-in-django/12758859        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


