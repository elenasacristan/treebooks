from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import LoginForm

# Create your views here.

def index(request):
    '''Return the home page'''
    return render(request, 'index.html')


def login(request):
    '''Return the login page'''
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
            else:
                login_form.add_error(None, 'Your username or password is incorrect')
    else:
        '''if the method is not POST we pass an empty form'''
        login_form = LoginForm()

    return render(request, 'login.html', {'login_form':login_form})    
    

def logout(request):
    '''Log the user out / request contains the user object'''
    auth.logout(request)
    messages.success(request,'You have been succesfully loged out')
    return redirect (reverse('index'))

