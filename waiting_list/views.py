from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
from books.models import Book
from .models import WaitingList
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseRedirect


# Create your views here.
@login_required
def view_waiting_lists(request, pk):
    waiting_list = WaitingList.objects.filter(wl_book__id = pk).distinct()
    return render (request, 'waiting_list.html',{'waiting_list':waiting_list})

@login_required
def join_waiting_list(request, pk):
    add_wl_book = get_object_or_404(Book,pk=pk)

    if request.method == 'POST':
        user = request.user
        user_already_in_list = WaitingList.objects.filter(wl_user=user, wl_book=add_wl_book)

        if user_already_in_list:
            messages.success(request, 'Your name is already in the waiting list')
        
        else:
            waiting_list, created = WaitingList.objects.get_or_create(
                wl_book = add_wl_book
            )
            waiting_list = get_object_or_404(WaitingList, wl_book = add_wl_book)
            waiting_list.wl_user.add(user)
            waiting_list.save() 
            messages.success(request, 'You have been added to the waiting list')

    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


