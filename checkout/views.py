import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404

from cart.contexts import cart_contents
from services.models import Service
from .forms import OrderForm
from .models import OrderLineItem, Order


# Create your views here.
def checkout(request):

    # define stripe public & secret keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # get cart from session
        cart = request.session.get('cart', {})

        # get data submitted in form
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        # create order_form object
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    service = Service.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        service=service,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Service.DoesNotExist:
                    order.delete()
                    return redirect(reverse('cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
    else:
        # Handle GET requests

        # Verify existance of cart
        cart = request.session.get('cart', {})
        if not cart:
            return redirect(reverse('services'))

        # Get cart contents from context processor
        current_cart = cart_contents(request)

        # define and round total
        total = current_cart['total']
        stripe_total = round(total * 100)

        # create stripe intent
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='eur',
            payment_method_types=['card'],
        )

        # generate order form
        order_form = OrderForm()

        # render page
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, 'success')

    if 'cart' in request.session:
        del request.session['cart']

        template = 'checkout/checkout_success.html'
        context = {
            'order': order
        }

        return render(request, template, context)
