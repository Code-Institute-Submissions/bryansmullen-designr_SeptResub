from django.shortcuts import render, redirect


def cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    quantity = int(request.POST['quantity'])
    my_cart = request.session.get('cart', {})

    if item_id in list(my_cart.keys()):
        my_cart[item_id] += quantity
    else:
        my_cart[item_id] = quantity

    request.session['cart'] = my_cart
    print(request.session['cart'])
    return redirect(cart)


def remove_from_cart(request, item_id):
    redirect_url = request.POST['redirect_url']
    cart = request.session.get('cart', {})
    cart.pop(item_id)
    request.session['cart'] = cart
    return redirect(redirect_url)
