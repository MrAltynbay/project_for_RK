import factory
from factory.fuzzy import FuzzyDecimal

from core.models import Currency


class CurrencyFactory(factory.django.DjangoModelFactory):
    name = factory.faker.Faker("name")
    rate = FuzzyDecimal(0.5, 50.1234, 4)

    class Meta:
        model = Currency
