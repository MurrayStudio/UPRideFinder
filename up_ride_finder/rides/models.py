from django.db import models
from django.utils.translation import ugettext_lazy as _
from ..users.models import User


class Ride(models.Model):
    destination = models.IntegerField(_('ZIP code of final destination'))
    origin = models.IntegerField(_('ZIP code of origin'))
    available_seats = models.IntegerField(_('Maximum number of passengers'))
    cost = models.CharField(_('Approx. cost the driver expects riders to pay.'), max_length=255)
    when = models.DateTimeField(_('Approximate departure date and time'))
    trip_summary = models.CharField(_('Summary of the trip'), max_length=255)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver')
    riders = models.ManyToManyField(User, related_name='riders')
    trip_id = models.PositiveIntegerField(_('Trip ID'))

    def __str__(self):
        return self.trip_summary
