from datetime import datetime, timedelta

import pytz

from django.test import RequestFactory
from test_plus import TestCase

from ..forms import RideCreateForm, RideAdminForm


class TestRideForms(TestCase):

    # @classmethod
    # def setUpTestData(self):
    #     cls.ride = RideFactory.create()

    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()

    def test_clean_ride_success(self):
        when = datetime.now(pytz.timezone('America/Los_Angeles')) + timedelta(days=4)
        form_data = {
            'destination': '97203',
            'origin': '90210',
            'available_seats': '5',
            'cost': '$5',
            'when': str(when).split('.')[0],
            'trip_summary': 'Valid summary'
        }

        form = RideCreateForm(form_data)
        valid = form.is_valid()
        self.assertTrue(valid)

