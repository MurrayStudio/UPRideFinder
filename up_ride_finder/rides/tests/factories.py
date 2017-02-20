import factory
import pytz
from datetime import datetime
from ...users.tests.factories import UserFactory
from ...users.models import User


class RideFactory(factory.django.DjangoModelFactory):
    # set destination and origin in a (VERY) pseudo-random order
    destination = factory.Faker('zipcode')
    origin = factory.Faker('zipcode')
    available_seats = factory.Sequence(lambda n: (n % 10) + 1)
    cost = factory.Faker('sentence', nb_words=6)
    when = factory.Faker('date_time_this_decade', after_now=True, tzinfo=pytz.timezone('America/Los_Angeles'))
    trip_summary = factory.Faker('sentence', nb_words=6)
    driver = factory.SubFactory(UserFactory)
    # driver = factory.Iterator(User.objects.all())
    # riders = models.ManyToManyField(User, related_name='riders')
    # trip_id = models.PositiveIntegerField(_('Trip ID'))

    class Meta:
        model = 'rides.Ride'
