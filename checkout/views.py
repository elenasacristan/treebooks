from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from books.models import Book
from userprofile.models import UserProfile
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

'''
The user will need to be logged in
in order to make a payment
'''
@login_required
def checkout(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
        
            cart = request.session.get('cart',{})
            total = 0
            for id, days in cart.items():
                book = get_object_or_404(Book, pk=id)
                total += days * book.price_day
                order_line_item = OrderLineItem(
                    order = order,
                    book = book,
                    days = days
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = 'GBP',
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            # timedelta - https://stackoverflow.com/questions/27491248/django-default-timezone-now-delta
            if customer.paid:
                messages.error(request, "You have succesfully paid")
                '''save book in list of read books'''
                profile = UserProfile.objects.get(user = request.user)
                for id, days in cart.items():
                    book = get_object_or_404(Book, pk=id)
                    profile.read_books.add(book)
                    book.return_date = order.date + timezone.timedelta(days=days)
                    book.available = False
                    book.save()

                request.session['cart'] = {}
                return redirect(reverse('view_all_books'))
            
            else:
                messages.error(request, "Unable to make payment")
    
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, 'checkout.html', {'payment_form':payment_form, 'order_form':order_form, 'publishable':settings.STRIPE_PUBLISHABLE})
