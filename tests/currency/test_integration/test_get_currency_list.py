import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tests.factories.currency import CurrencyFactory
from tests.factories.user import UserFactory


@pytest.mark.django_db
@pytest.mark.parametrize(
    "currency_count",
    [1, 2, 3, 4, 5]
)
def test__get_currency_list__success_case(currency_count, api_client: APIClient) -> None:
    user = UserFactory.create()

    currencies = CurrencyFactory.create_batch(currency_count)

    api_client.force_authenticate(user)
    r = api_client.get(reverse("api:currencies-list"))
    r_data = r.json()

    assert r.status_code == status.HTTP_200_OK
    assert len(r_data) == len(currencies)


@pytest.mark.django_db
def test__get_currency_list__without_auth(api_client: APIClient) -> None:
    r = api_client.get(reverse("api:currencies-list"))

    assert r.status_code == status.HTTP_401_UNAUTHORIZED

