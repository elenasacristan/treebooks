from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from books.models import Book
from .forms import ReviewForm
from django.utils import timezone


# Create your views here.

@login_required
def add_review(request, pk):
    book = get_object_or_404(Book,pk=pk)
    book.save()

    if request.method == 'POST':
         review_form = ReviewForm(request.POST)

         if review_form.is_valid():
             review = review_form.save(commit=False)
             review.date = timezone.now()
             review.review_author = request.user
             review.reviewed_book = book
             review.save()
             return redirect(reverse('view_profile'))
    
    else:
        review_form = ReviewForm()
    return render(request, 'review_form.html', {'review_form':review_form})
