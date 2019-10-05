from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserProfileForm
from django.utils import timezone


# Create your views here.

@login_required
def view_profile(request):
    user_profile = User.objects.get(email=request.user.email)
    user_profile.save()
    current_books = user_profile.profile.read_books.filter(return_date__gt = timezone.now())
    return render(request, 'view_profile.html', {'user_profile':user_profile, 'current_books':current_books})

@login_required
def edit_user_profile(request, id):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user.profile ,data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile'))
    
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_user_profile.html', {'form':form})


