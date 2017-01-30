# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
# from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)

    def clean_email(self, email):
        """
        Checks that entered email ends in '@up.edu'.
        """
        if not email.endswith('@up.edu'):
            raise forms.ValidationError("Not an @up.edu email address.")
        return email


# class SocialAccountAdapter(DefaultSocialAccountAdapter):
#     def is_open_for_signup(self, request, sociallogin):
#         return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)
