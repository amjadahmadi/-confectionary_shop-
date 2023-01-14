import re
from django.core.exceptions import ValidationError


def test(val):
    if not re.fullmatch('(\+98|0)\d{10}', val):
        raise ValidationError('Disallowed number')
