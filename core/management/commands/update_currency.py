import xml.etree.ElementTree as ET
from decimal import Decimal

import requests
from django.core.management import BaseCommand

from core.models import Currency
from project_for_RK.settings import CURRENCY_DATA_URL


class Command(BaseCommand):
    help = 'Update Currency table'

    def handle(self, *args, **options):

        response = requests.get(CURRENCY_DATA_URL)

        if response.status_code == 200:
            xml_data = ET.fromstring(response.text)

            currencies_to_update = []
            currencies_to_create = []

            for valute in xml_data.findall('Valute'):
                currency_name = valute.find('Name').text
                currency_value = Decimal(valute.find('Value').text.replace(',', '.'))

                try:
                    currency = Currency.objects.get(name=currency_name, rate=currency_value)
                except Currency.DoesNotExist:
                    currencies_to_create.append(Currency(name=currency_name, rate=currency_value))
                    continue

                currencies_to_update.append(currency)

            if currencies_to_update:
                Currency.objects.bulk_update(currencies_to_update, fields=['name', 'rate'])

            if currencies_to_create:
                Currency.objects.bulk_create(currencies_to_create)

            self.stdout.write(self.style.SUCCESS('Records updated successfully'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch XML file'))
