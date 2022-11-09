from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def min_contribution(value):
    if value<1000000:
        raise ValidationError(
            _('Minimum contribution can be 1.000.000 or more. %(value) is less than 1.000.000'),
            params={'value': value},
        )