import factory
from datetime import datetime
from ...users.tests.factories import UserFactory


# class RideFactory(factory.django.DjangoModelFactory):
#     # set destination and origin in a (VERY) pseudo-random order
#     destination = factory.Sequence(lambda n: (394820394 * n) % 99999)
#     origin = factory.Sequence(lambda n: (93842053 * n) % 99999)
#     available_seats = factory.Sequence(lambda n: n % 10)
#     cost = "About tree fiddy"
#     when = datetime(2017, 04, 11).isoformat()
#     trip_summary = "Example summary"
#     driver = factory.SubFactory(UserFactory)
#     # riders = models.ManyToManyField(User, related_name='riders')
#     trip_id = models.PositiveIntegerField(_('Trip ID'))

#     class Meta:
#         model = 'rides.Ride'
