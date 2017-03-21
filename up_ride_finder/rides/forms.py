from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Ride, RideRequest


class RideAdminForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = '__all__'

    def clean(self):
        """Prevent the driver from being a rider """
        driver = self.cleaned_data.get('driver')
        riders = self.cleaned_data.get('riders')
        if driver in riders:
            raise ValidationError(_('Trip driver cannot be a rider.'))
        return self.cleaned_data


class RideRequestAdminForm(forms.ModelForm):
    class Meta:
        model = RideRequest
        fields = '__all__'

    def clean(self):
        """Prevent the driver from being a requester """
        ride = self.cleaned_data.get('ride')
        requester = self.cleaned_data.get('requester')
        if requester == ride.driver:
            raise ValidationError(_('Trip driver cannot be a requester.'))
        return self.cleaned_data


class RideCreateForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['destination', 'origin', 'available_seats', 'cost', 'when', 'trip_summary']

    # def clean(self):
    #     """ Prevent the driver from being a rider """
    #     driver = self.cleaned_data.get('driver')
    #     riders = self.cleaned_data.get('riders')
    #     if driver in riders:
    #         raise ValidationError(_('Trip driver cannot be a rider.'))
    #     return self.cleaned_data
