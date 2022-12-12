import random
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder": "your first name"}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder": "your last name"}))
    phone = forms.CharField(max_length=12, validators=[RegexValidator(r'^(\+98|0)\d{10}')], widget=forms.TextInput(
        attrs={
            "placeholder": "your phone"
        }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password Confirmation'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['phone'].label = 'phone'
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name', 'password1', 'password2')
        help_texts = {
            'username': None,
        }


class CodeForm(forms.Form):
    valid_code = forms.CharField(max_length=4,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'enter send code on your phone.', 'style': '"margin: 0"'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['valid_code'].label = 'validation code'


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=12, label='phone', validators=[RegexValidator(r'^(\+98|0)\d{10}')],
                            widget=forms.TextInput(
                                attrs={'placeholder': 'enter your phone.', 'style': '"margin: 0"'}))
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'enter your password.', 'style': '"margin: 0"'}))




