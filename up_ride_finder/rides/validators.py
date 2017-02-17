# from datetime import datetime
from string import digits

from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def future_date(date):
    if date <= timezone.now():
        raise ValidationError(_('Trip must be scheduled for a future date.'))


def valid_zip(zipcode):
    if len(zipcode) != 5:
        raise ValidationError(_('Zip codes must be 5 characters long.'))
    if not all([d in digits for d in zipcode]):
        raise ValidationError(_('Zip codes must consist exclusively of digits.'))