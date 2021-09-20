import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from cart.contexts import cart_contents
from services.models import Service
from .forms import OrderForm
from .models import OrderLineItem, Order
from profiles.models import UserProfile
import json
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
@require_POST
def cache_checkout_data(request):
    """
    Temporarily cache checkout data for stripe workflow
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'username': request.user,
        })

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


# Create your views here.
def checkout(request):
    """
    Display checkout page
    """
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
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()

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
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

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
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')
        # render page
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret
        }

        return render(request, template, context)


@login_required(login_url='/accounts/login/')
def checkout_success(request, order_number):
    """
    Display checkout success page
    """
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        order = get_object_or_404(Order, order_number=order_number)
    messages.success(
        request, 'Order processed successfully! Your order number is' +
        f'{order_number}. We will be in touch with you shortly!')

    if 'cart' in request.session:
        del request.session['cart']

        template = 'checkout/checkout_success.html'
        context = {
            'order': order
        }

        return render(request, template, context)
