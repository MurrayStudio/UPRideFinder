from django import forms
from django.conf import settings
from test_plus.test import TestCase
from ..adapters import AccountAdapter


class TestUserSignUpForm(TestCase):
    """
    Test the user sign-up validation.
    """
    def setUp(self):
        self.valid_email = 'valid@up.edu'
        self.invalid_email = 'invalid@notup.biz'
        self.AccAdapter = AccountAdapter()

    def test_open_for_signup(self):
        """
        Pretty trivial for now.
        """
        self.assertEqual(self.AccAdapter.is_open_for_signup(None),
                         getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True))

    def test_valid_email(self):
        """
        Tests if a valid email (valid@up.edu) is accepted as valid
        """
        self.assertEqual(
            self.AccAdapter.clean_email(self.valid_email), self.valid_email)

    def test_invalid_email(self):
        """
        Tests if an invalid email is rejected as invalid.
        """
        self.assertRaises(
            forms.ValidationError,
            self.AccAdapter.clean_email,
            email=self.invalid_email)
