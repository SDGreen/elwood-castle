from django import forms
from .models import UserAccount


class UserForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholder = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Delivery Email',
            'phone_number': 'Contact Number'
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = f'{placeholder[field]}'
            self.fields[field].widget.attrs['class'] = 'checkout-form-input body-text text-m'
            self.fields[field].label = False
