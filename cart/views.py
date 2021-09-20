from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def cart(request):
    """
    Display cart page
    """
    return render(request, 'cart/cart.html')


@login_required(login_url='/accounts/login/')
def add_to_cart(request, item_id):
    """
    Add item to cart and display cart page
    """
    quantity = int(request.POST['quantity'])
    my_cart = request.session.get('cart', {})

    if item_id in list(my_cart.keys()):
        my_cart[item_id] += quantity
    else:
        my_cart[item_id] = quantity

    request.session['cart'] = my_cart
    return redirect(cart)


@login_required(login_url='/accounts/login/')
def remove_from_cart(request, item_id):
    """
    Remove item from cart and redirect
    """
    redirect_url = request.POST['redirect_url']
    cart = request.session.get('cart', {})
    cart.pop(item_id)
    request.session['cart'] = cart
    return redirect(redirect_url)
