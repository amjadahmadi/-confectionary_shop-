import random
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as we
from .models import User, Comment


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder": _("your first name")}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder": _("your last name")}))
    phone = forms.CharField(max_length=12, validators=[RegexValidator(r'^(\+98|0)\d{10}')], widget=forms.TextInput(
        attrs={
            "placeholder": _("your phone here")
        }))

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": _("your password")}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": _("Repeat your password")}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = _('Password')
        self.fields['password2'].label = _('Password Confirmation')
        self.fields['first_name'].label = _('First Name')
        self.fields['last_name'].label = _('Last Name')
        self.fields['phone'].label = _('phone 2')
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
                                     attrs={'placeholder': _('enter send code on your phone.'),
                                            'style': '"margin: 0"'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['valid_code'].label = _('validation code')


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=12, label=_('phone'), validators=[RegexValidator(r'^(\+98|0)\d{10}')],
                            widget=forms.TextInput(
                                attrs={'placeholder': _('enter your phone.'), 'style': '"margin: 0"'}))
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': _('enter your password.'), 'style': '"margin: 0"'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
            'content_type': forms.HiddenInput(),
            'status': forms.HiddenInput(),
            'is_deleted': forms.HiddenInput()
        }
        labels = {
            'first_name': _('first name'),
            'last_name': _('last name'),
            'comment_body': _("your comment"),
            'email': _('email'),
            'rate':_('Rate')
        }
