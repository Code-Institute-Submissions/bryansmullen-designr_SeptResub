from django.conf import settings


def cart_contents(request):
    cart_items = []
    subtotal = 0
    product_count = 0
    vat = subtotal * settings.VAT_RATE_PERCENTAGE
    total = subtotal + vat

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'product_count': product_count,
        'vat': vat,
        'total': total
    }

    return context
