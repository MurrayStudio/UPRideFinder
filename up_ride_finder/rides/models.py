from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from ..users.models import User
from .validators import valid_zip, future_date


class Ride(models.Model):
    destination = models.CharField(_('ZIP code of final destination'), max_length=5, validators=[valid_zip])
    origin = models.CharField(_('ZIP code of origin'), max_length=5, validators=[valid_zip])
    available_seats = models.IntegerField(_('Maximum number of passengers'), validators=[MinValueValidator(1)])
    cost = models.CharField(_('Approx. cost the driver expects riders to pay.'), max_length=255)
    when = models.DateTimeField(_('Approximate departure date and time'), validators=[future_date])
    trip_summary = models.CharField(_('Summary of the trip'), max_length=255)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver')
    riders = models.ManyToManyField(User, related_name='riders', blank=True)
    created_date = models.DateTimeField(_('Date created'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Date modified'), auto_now=True)
    # trip_id = models.PositiveIntegerField(_('Trip ID'))
    # Django has an automatic id field

    def __str__(self):
        return self.trip_summary
