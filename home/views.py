from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactUsForm
from .models import TotalRaised
from django.utils import timezone
from django.contrib import auth, messages



# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def donate(request):
    return render(request, 'donate.html')

def projects(request):
    raised = get_object_or_404(TotalRaised, pk=1)
    return render(request, 'projects.html', {'raised':raised})
    
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