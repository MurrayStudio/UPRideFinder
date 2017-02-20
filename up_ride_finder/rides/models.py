# from geopy.geocoders import GoogleV3
import googlemaps

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.conf import settings

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

    dest_name = models.CharField(_('Friendly name of final destination'), max_length=255, blank=True)
    origin_name = models.CharField(_('Friendly name of origin'), max_length=255, blank=True)
    # trip_id = models.PositiveIntegerField(_('Trip ID'))
    # Django has an automatic id field

    def __str__(self):
        return "({}) {} to {}".format(self.id, self.origin_name, self.dest_name)

    def get_absolute_url(self):
        return reverse('rides:detail', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        """
        Set the origin and destination to friendlier names if possible.
        """
        if not self.dest_name or not self.origin_name:
            gmaps = googlemaps.Client(key=getattr(settings, 'GOOGLE_MAPS_GEOCODING_KEY', None), timeout=5)
            if not self.dest_name:
                gmaps_results = gmaps.geocode(self.destination)
                dest_name = ''
                if len(gmaps_results):
                    dest_name = gmaps_results[0].get('formatted_address')
                if 'USA' in dest_name:
                    self.dest_name = dest_name
                else:
                    self.dest_name = self.destination
            if not self.origin_name:
                gmaps_results = gmaps.geocode(self.origin)
                origin_name = ''
                if len(gmaps_results):
                    origin_name = gmaps_results[0].get('formatted_address')
                if 'USA' in origin_name:
                    self.origin_name = origin_name
                else:
                    self.origin_name = self.origin

        super(Ride, self).save(*args, **kwargs)  # Call the real save() method
