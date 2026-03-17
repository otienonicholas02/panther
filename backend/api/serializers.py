from rest_framework import serializers
from .models import User, Shipment, Delivery

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    user_type = serializers.ChoiceField(choices=['customer', 'driver', 'admin'])
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)

class ShipmentSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    tracking_number = serializers.CharField(read_only=True)
    sender = serializers.CharField()
    recipient_name = serializers.CharField(max_length=200)
    recipient_phone = serializers.CharField(max_length=20)
    recipient_email = serializers.EmailField()
    origin_address = serializers.CharField()
    destination_address = serializers.CharField()
    weight = serializers.FloatField()
    status = serializers.ChoiceField(choices=['pending', 'picked_up', 'in_transit', 'delivered', 'cancelled'])
    shipping_cost = serializers.FloatField()
    created_at = serializers.DateTimeField(read_only=True)

class DeliverySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    shipment = serializers.CharField()
    driver = serializers.CharField(required=False)
    current_location = serializers.CharField(required=False)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    estimated_delivery_time = serializers.DateTimeField(required=False)
    actual_delivery_time = serializers.DateTimeField(required=False)
    delivery_notes = serializers.CharField(required=False)
