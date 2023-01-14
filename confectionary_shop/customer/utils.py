from .forms import CommentForm
from product.models import Stock
from django import forms
from django.contrib.contenttypes.models import ContentType


def create_comment_form(request, object_id):
    f = CommentForm()
    stock = ContentType.objects.get_for_model(Stock).pk
    initial = {'object_id': object_id, 'content_type': stock}
    f.fields['first_name'].widget.attrs['required'] = True
    f.fields['last_name'].widget.attrs['required'] = True
    f.fields['email'].widget.attrs['required'] = True

    if request.user.is_authenticated:
        initial.update(
            {'first_name': request.user.first_name, 'last_name': request.user.last_name, 'user': request.user, 'email': 'sample@email.com'})
        f.fields['first_name'].widget.attrs['readonly'] = True
        f.fields['last_name'].widget.attrs['readonly'] = True
        f.fields['email'].widget = forms.HiddenInput()
    # f.fields['content_type'].widget = forms.HiddenInput()
    f.initial = initial
    return f
