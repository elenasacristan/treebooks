from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, UserProfileForm
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def index(request):
    '''Return the home page'''
    return render(request, 'index.html')


def login(request):
    '''Return the login page'''
    if request.user.is_authenticated:
        return redirect(reverse ('index'))

    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            '''This code will check if the username and password are correct'''
            user = auth.authenticate(username = request.POST['username'],
                                    password = request.POST['password'])
            
            if user:
                '''if password and username are correct we log the user in'''
                auth.login(request=request, user=user)
                messages.success(request, 'You have successfully login')
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'Your username or password is incorrect')
    else:
        '''if the method is not POST we pass an empty form'''
        login_form = LoginForm()

    return render(request, 'login.html', {'login_form':login_form})    
    
@login_required
def logout(request):
    '''Log the user out / request contains the user object'''
    auth.logout(request)
    messages.success(request,'You have been succesfully loged out')
    return redirect (reverse('index'))


def registration(request):
    '''Registration page'''

    '''If the user is already logged in it redirects them to the index page'''
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if registration_form.is_valid() and profile_form.is_valid():
            user = registration_form.save()

            '''Now I create a new profile using the data from the form 
            I use commit=False so I don't save it to the db'''
            profile = profile_form.save(commit=False)

            '''Here is we we indicate the OneToOne'''
            profile.user = user

            '''This should save my user'''
            profile.save()

            '''Checks that user and password are valid and if
            they are returns a User object'''
            user = auth.authenticate(username = request.POST['username'],
                                    password = request.POST['password1'])
            
            if user:
                '''If the user and password are correct the log the user in'''
                auth.login(request=request, user=user)
                messages.success(request, 'You have been succesfully registered')
                return redirect(reverse('index'))
            else:
                messages.error(request, 'We were unable to register your account at this time')
    else:
        registration_form = RegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'registration.html', {'registration_form':registration_form, 'profile_form':profile_form})

@login_required
def user_profile(request):
    '''The user profile page'''
    profile = Profile.objects.get(user__email=request.user.email)
    
    return render(request, 'profile.html', {'profile':profile})

