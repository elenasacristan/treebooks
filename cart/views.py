from django.shortcuts import render, redirect, reverse


# Create your views here.
'''
We don't need to pass the cart as a dictionary because
the cart is available from everywhere
'''
def view_cart(request):
    return render(request, 'cart.html')

def add_to_cart(request, id):

    '''
    Add number of days to read the book
    '''
    days = int(request.POST.get('days'))

    cart = request.session.get('cart',{})

    '''
    if the book haven't been added to the cart
    yet it will be added
    '''
    if id not in cart:
        cart[id] = cart.get(id, days)

    '''
    saves the cart into the session
    '''
    request.session['cart'] = cart

    return redirect('detail', id)
    # return redirect(reverse('view_Cart'))



def adjust_cart(request, id):
    '''
    Adjust the number of days that the user
    wants to rent the book for
    '''
    days = int(request.POST.get('days'))
    cart = request.session.get('cart',{})

    if days > 0:
        cart[id] = days
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

   
