from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'phone_number',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Contact Number'
        }

        placeholder = {
            'first_name': 'John...',
            'last_name': 'Elwood...',
            'email': 'example@example.com',
            'phone_number': '07875269520...'
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                self.fields[field].label = f"{labels[field]} "
            else:
                self.fields[field].label = f"{labels[field]}"
            self.fields[field].widget.attrs['class'] = 'checkout-form-input body-text text-m'
            self.fields[field].widget.attrs['placeholder'] = f'{placeholder[field]}'
