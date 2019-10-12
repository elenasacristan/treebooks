from django.shortcuts import render, redirect, reverse
from .forms import ContactUsForm
from django.utils import timezone
from django.contrib import auth, messages



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
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.contact_date = timezone.now()
            contact.save()
            messages.success(request, 'We have received your request and we will be in touch shortly')
            return redirect(reverse('index'))

    else:
        contact_form = ContactUsForm()

    return render(request, 'contact.html', {'contact_form':contact_form})