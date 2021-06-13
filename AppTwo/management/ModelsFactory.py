import factory
from AppTwo.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        # Unique attrs in here
        django_get_or_create = ('first_name',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
