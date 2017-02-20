from test_plus import TestCase

from .factories import RideFactory


class TestUser(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ride_valid_zip = RideFactory.create(destination='98466', origin='90210')
        cls.ride_invalid_zip = RideFactory.create(destination='11111', origin='22222')

    def test__str__valid_zip(self):
        should_str = '({}) Beverly Hills, CA 90210, USA to Tacoma, WA 98466, USA'.format(self.ride_valid_zip.id)
        self.assertEqual(self.ride_valid_zip.__str__(), should_str)

    def test_get_absolute_url(self):
        self.assertEqual(
            self.ride_valid_zip.get_absolute_url(),
            '/rides/{}/'.format(self.ride_valid_zip.id)
        )
