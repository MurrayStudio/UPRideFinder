from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Ride


class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = '__all__'

    def clean(self):
        """ Prevent the driver from being a rider """
        driver = self.cleaned_data.get('driver')
        riders = self.cleaned_data.get('riders')
        if driver in riders:
            raise ValidationError(_('Trip driver cannot be a rider.'))
        return self.cleaned_data
