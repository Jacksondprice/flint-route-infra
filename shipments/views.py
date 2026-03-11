from rest_framework import viewsets

from .models import Shipment
from .serializers import ShipmentSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.order_by("id")
    serializer_class = ShipmentSerializer
