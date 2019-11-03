from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
'''
We don't need to pass the cart as a dictionary because
the cart is available from everywhere.
@login_required so only authenticated users can view the cart
'''
@login_required
def view_cart(request):
    #Returns the cart
    return render(request, 'cart.html')


'''
@login_required so only authenticated users can add book to the cart
'''
@login_required
def add_to_cart(request, id):

    # Add number of days to read the book
    days = int(request.POST.get('days'))
    cart = request.session.get('cart',{})

    # If the book haven't been added to the cart yet it will be added
    if id in cart:
        messages.success(request, 'This book is already added to cart')
    else:
        messages.success(request, 'Book succesfully added to the cart')
        cart[id] = cart.get(id, days)

    # Saves the cart into the session
    request.session['cart'] = cart
    return redirect('detail', id)


'''
Adjust the number of days that the user wants to rent the book for.
@login_required so only authenticated users can adjust the days
'''
@login_required
def adjust_cart(request, id):

    days = int(request.POST.get('days'))
    cart = request.session.get('cart',{})

    if days > 0:
        cart[id] = days
    else:
        cart.pop(id)

    # Saves the cart into the session
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


'''
Remove a book from the cart clicking the trash button.
@login_required so only authenticated users can remove books from cart
'''
@login_required
def remove_from_cart(request, id):
    cart = request.session.get('cart',{})

    # Removes book from cart
    cart.pop(id)
    
    # Saves the cart into the session
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))