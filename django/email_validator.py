"""Email field validator."""

#1 forms.py

from django import forms
from django.forms import Form, ModelForm
from django.core.validators import EmailValidator


class ContactForm(Form):
    full_name = forms.CharField(
            label = 'Full Name',
            help_text = 'Enter your full name, first and last name please',
            min_length = 2,
            max_length = 300,
            required = True,
            error_messages = {
                'required': 'Please provide us with a name to 
                address you as',
                'min_length': 'Please lengthen your name, min 2 characters',
                'max_length': 'Please shorten your name, max 300 characters',
                }
            ),
            widget = forms.TextInput(
                attrs = {
                    'id': 'full-name',
                    'class': 'form-input-class',
                    'placeholder': 'Your Name, Written By...'
                }
            ),
            email_1 = forms.CharField(
                    label = 'email_1 Field',
                    min_length = 5,
                    max_length = 254,
                    required = False,
                    help_text = 'Email address in example@example.com
                    format.',
                    validators = [
                        EmailValidator(
                            'Please enter a valid email address'
                        ),
                    ],
                    error_messages = {
                        'min_length': 'Please lengthen your name, min
                        5 characters',
                        'max_length': 'Please shorten your name, max
                        254 characters'
                    },
            )

            email_2 = forms.EmailField(
                    label = 'email_2 Field',
                    min_length = 5,
                    max_length = 254,
                    required = True,
                    help_text = 'Email address in example@example.com
                    format for contacting you should we have questions about
                    your message.',
                    error_messages = {
                        'required': 'Please provide us an email
                        address should we need to reach you',
                        'email': 'Please enter a valid email address',
                        'min_length': 'Please lengthen your name, min
                        5 characters',
                        'max_length': 'Please shorten your name, max
                        254 characters'
                        }
                    )

    
