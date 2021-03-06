from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Service


def cart_contents(request):
    """
    Shopping Cart Context To Access Cart Items etc
    """
    cart_items = []
    subtotal = 0
    vat = subtotal * settings.VAT_RATE_PERCENTAGE
    total = subtotal + vat
    cart = request.session.get('cart', {})

    for id, quantity in cart.items():
        service = get_object_or_404(Service, pk=id)
        subtotal += quantity * service.price
        vat = round(subtotal * settings.VAT_RATE_PERCENTAGE)
        total = subtotal + vat
        cart_items.append({
            'id': id,
            'quantity': quantity,
            'service': service
        })

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'vat': vat,
        'total': total
    }

    return context
