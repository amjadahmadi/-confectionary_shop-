from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Cake_Designing, Feeling
from datetime import datetime, timedelta


class CakeDesigningForm(forms.ModelForm):
    class Meta:
        model = Cake_Designing
        fields = '__all__'
        widgets = {
            'sample_img': forms.FileInput(
                attrs={'class': 'form-control'}),
            'print_img': forms.FileInput(
                attrs={'class': 'form-control'}),
            'ready_time': forms.TimeInput(attrs={'class': 'form-control', 'readonly': True,
                                                 'value': (datetime.now() + timedelta(days=3)).strftime('%d/%m/%Y')}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'payment_status': forms.TextInput(
                attrs={'class': 'form-control', 'readonly': True}),
            'extra_payment': forms.TextInput(
                attrs={'class': 'form-control', 'readonly': True, 'placeholder': _('after review will be showed')}),
            'feeling_id': forms.Select(
                attrs={'class': 'form-control', 'placeholder': _('choice your feeling want')}),
            'taste_id': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'readonly': True, 'value': 180000}),
            'amount': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': _('The amount of weight you want')}),
            'order_id': forms.HiddenInput(),
            'is_deleted': forms.HiddenInput()

        }
        labels = {
            'sample_img': _('sample image'),
            'print_img': _('printing image'),
            'ready_time': _('ready time'),
            'description': _('description'),
            'payment_status': _('payment status'),
            'extra_payment': _('extra payment'),
            'feeling_id': _('felling'),
            'taste_id': _('taste'),
            'price': _('price / each kilo (180000 IR)'),
            'amount': _('amount'),
        }
