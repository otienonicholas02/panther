from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Shipment, Delivery
from .serializers import UserSerializer, ShipmentSerializer, DeliverySerializer

class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for User model"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        """Register a new user"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class ShipmentViewSet(viewsets.ModelViewSet):
    """ViewSet for Shipment model"""
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    @action(detail=False, methods=['get'])
    def track(self, request):
        """Track shipment by tracking number"""
        tracking_number = request.query_params.get('tracking_number')
        try:
            shipment = Shipment.objects.get(tracking_number=tracking_number)
            serializer = self.get_serializer(shipment)
            return Response(serializer.data)
        except Shipment.DoesNotExist:
            return Response({'error': 'Shipment not found'}, status=404)

class DeliveryViewSet(viewsets.ModelViewSet):
    """ViewSet for Delivery model"""
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
