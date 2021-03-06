from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    """
    This class defines the form used for order forms
    """
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number', 'street_address1',
            'street_address2', 'town_or_city', 'postcode', 'country', 'county')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'country': 'Country',
            'postcode': 'Post Code',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            if field != 'country':
                self.fields[field].widget.attrs['placeholder'] = (
                    placeholder
                    )
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
