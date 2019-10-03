from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from books.models import Book

# Create your views here.

   
def see_favourites(request):
    userprofile = UserProfile.objects.get(user = request.user)
    favourites = userprofile.favourites.all()
    return render(request, 'favourites.html', {'favourites':favourites})

'''
if the book is already saved as favourite then
remove it from favourites.
If the book is not saved as favourite then
save it as favourite
'''
def add_remove_favourites(request, id):
    book = get_object_or_404(Book,pk=id)

    if request.method == 'POST':
        profile = UserProfile.objects.get(user = request.user)
        fav_book = Book.objects.get(pk=id)
        
        if fav_book in profile.favourites.all():
            profile.favourites.remove(fav_book)
        else:
            profile.favourites.add(fav_book)
    
    return render(request, 'detail.html', {'book':book})

