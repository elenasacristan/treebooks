from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.

def index(request):
    '''Return the home page'''
    return render(request, 'index.html')

def login(request):
    '''Return the login page'''
    return render(request, 'login.html')

def logout(request):
    '''Log the user out / request contains the user object'''
    auth.logout(request)
    messages.success(request,'You have been succesfully loged out')
    return redirect (reverse('index'))

