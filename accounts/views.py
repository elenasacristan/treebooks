from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm

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
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username = request.POST['username'],
                                    password = request.POST['password1'])
            
            if user:
                auth.login(request=request, user=user)
                messages.success(request, 'You have been succesfully registered')
                return redirect(reverse('index'))
            else:
                messages.error(request, 'We were unable to register your account at this time')
    else:
        registration_form = RegistrationForm()
    
    return render(request, 'registration.html', {'registration_form':registration_form})

