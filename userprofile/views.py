from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserProfileForm

# Create your views here.

@login_required
def view_profile(request):
    user_profile = User.objects.get(email=request.user.email)
    return render(request, 'view_profile.html', {'user_profile':user_profile})

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


