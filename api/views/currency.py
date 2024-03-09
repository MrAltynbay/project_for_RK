from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.currency import CurrencySerializer
from core.models import Currency


class CurrencyViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated, ]

    def list(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            currency = Currency.objects.get(id=pk)
            serializer = CurrencySerializer(currency)
            result = Response(serializer.data)
        except Currency.DoesNotExist:
            result = Response({'error': 'Currency not found'}, status=404)

        return result
