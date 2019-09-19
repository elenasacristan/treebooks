from django.shortcuts import render
# Create your views here.

def index(request):
    '''Return the home page'''
    return render(request, 'index.html')

def about(request):
    '''Return the home page'''
    return render(request, 'about.html')

def donate(request):
    '''Return the home page'''
    return render(request, 'donate.html')

def projects(request):
    '''Return the home page'''
    return render(request, 'projects.html')
    
def contact(request):
    '''Return the home page'''
    return render(request, 'contact.html')