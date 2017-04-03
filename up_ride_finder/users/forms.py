from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import User


class SignUpForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        label='Your Name',
        widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    phone = forms.CharField(
        max_length=10,
        label='Your Phone Number',
        widget=forms.TextInput(attrs={'placeholder': 'Your phone number'}))

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.phone = self.cleaned_data['phone']
        user.save()
