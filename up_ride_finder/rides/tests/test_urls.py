from django.core.urlresolvers import reverse, resolve

from test_plus.test import TestCase

from .factories import RideFactory


class TestRideURLs(TestCase):
    """Test URL patterns for rides."""

    @classmethod
    def setUpTestData(cls):
        cls.ride = RideFactory.create()

    def test_list_reverse(self):
        """rides:list should reverse to /rides/."""
        self.assertEqual(reverse('rides:list'), '/rides/')

    def test_list_resolve(self):
        """/rides/ should resolve to rides:list."""
        self.assertEqual(resolve('/rides/').view_name, 'rides:list')

    def test_detail_reverse(self):
        """rides:detail should reverse to /rides/{{ride.id}}/."""
        self.assertEqual(
            reverse('rides:detail', kwargs={'id': self.ride.id}),
            '/rides/{}/'.format(self.ride.id)
        )

    def test_detail_resolve(self):
        """/rides/{{ride.id}}/ should resolve to rides:detail."""
        self.assertEqual(resolve('/rides/{}/'.format(self.ride.id)).view_name, 'rides:detail')
