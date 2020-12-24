from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    user_email = forms.EmailField(max_length=200, required=True)
    subject = forms.CharField(max_length=200, required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if not subject:
            subject = "Customer Inquiry - From Elwood Website"
        return subject

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholder = {
            'user_email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['user_email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                self.fields[field].widget.attrs['placeholder'] = f'{placeholder[field]} *'
            else:
                self.fields[field].widget.attrs['placeholder'] = f'{placeholder[field]}'
            self.fields[field].widget.attrs['class'] = 'body-text text-m'
            self.fields[field].label = False
