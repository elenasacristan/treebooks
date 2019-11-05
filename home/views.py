from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactUsForm
from .models import TotalRaised, Projects
from django.utils import timezone
from django.contrib import auth, messages

# Create your views here.

def index(request):
    '''
    returns the home page (index.html)
    '''
    return render(request, 'index.html')


def about(request):
    '''
    returns the about page
    '''
    return render(request, 'about.html')


def donate(request):
    '''
    returns the donate page
    '''
    return render(request, 'donate.html')


def projects(request):
    '''
    Returns the project page and displays total money raised and books rented.
    if TotalRaised doesn't exist yet it will create it for the first time 
    and will be initialised to number_books=0 and money_raised=0.00
    '''
    totalraised, created = TotalRaised.objects.get_or_create(number_books=0, money_raised=0.00)

    raised = get_object_or_404(TotalRaised, pk=1)
    projects = Projects.objects.all()
    return render(request, 'projects.html', {'raised':raised, 'projects':projects})
    

def contact(request):
    '''Returns the contact us form page'''
    
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