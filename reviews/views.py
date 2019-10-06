from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ReviewForm
from django.utils import timezone


# Create your views here.

@login_required
# def add_review(request, id):
def add_review(request):

    # if request.method == 'POST':
    #     form = UserProfileForm(instance=request.user.profile ,data=request.POST, files=request.FILES)

    #     if form.is_valid():
    #         form.save()
    #         return redirect(reverse('view_profile'))
    
    # else:
    #     user = request.user
    #     profile = user.profile
    #     form = UserProfileForm(instance=profile)

    # return render(request, 'edit_user_profile.html', {'form':form})
    review_form = ReviewForm()
    return render(request, 'review_form.html', {'review_form':review_form})
