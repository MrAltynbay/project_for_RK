from decimal import Decimal

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tests.factories.currency import CurrencyFactory
from tests.factories.user import UserFactory


@pytest.mark.django_db
def test__get_currencies__own_currency(api_client: APIClient) -> None:
    user = UserFactory.create()
    currency = CurrencyFactory.create()

    api_client.force_authenticate(user)
    r = api_client.get(reverse("api:currencies-detail", args=[currency.pk]))
    r_data = r.json()

    assert r.status_code == status.HTTP_200_OK
    assert r_data["id"] == currency.pk
    assert r_data["name"] == currency.name
    assert Decimal(r_data["rate"]) == currency.rate


@pytest.mark.django_db
def test__get_currencies__not_exists_currency(api_client: APIClient) -> None:
    user = UserFactory.create()

    api_client.force_authenticate(user)
    r = api_client.get(reverse("api:currencies-detail", args=[123]))

    assert r.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test__get_currencies__without_auth(api_client: APIClient) -> None:
    r = api_client.get(reverse("api:currencies-detail", args=[123]))

    assert r.status_code == status.HTTP_401_UNAUTHORIZED
