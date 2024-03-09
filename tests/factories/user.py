import factory
from django.contrib.auth.models import User

from tests.factories.mixins import UniqueStringMixin


class UserFactory(factory.django.DjangoModelFactory):
    username = UniqueStringMixin("first_name")

    class Meta:
        model = User
