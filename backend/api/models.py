from mongoengine import Document, StringField, EmailField, IntField, FloatField, DateTimeField, BooleanField, ReferenceField, ListField
from datetime import datetime

class User(Document):
    """User model for customers and drivers"""
    email = EmailField(unique=True, required=True)
    username = StringField(unique=True, required=True)
    phone = StringField(required=True)
    first_name = StringField()
    last_name = StringField()
    password = StringField(required=True)
    user_type = StringField(choices=['customer', 'driver', 'admin'], default='customer')
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'users',
        'indexes': ['email', 'username', 'user_type']
    }

class Shipment(Document):
    """Shipment model for tracking logistics"""
    tracking_number = StringField(unique=True, required=True)
    sender = ReferenceField(User, required=True)
    recipient_name = StringField(required=True)
    recipient_phone = StringField(required=True)
    recipient_email = EmailField()
    origin_address = StringField(required=True)
    destination_address = StringField(required=True)
    weight = FloatField()  # in kg
    dimensions = StringField()
    status = StringField(choices=['pending', 'picked_up', 'in_transit', 'delivered', 'cancelled'], default='pending')
    shipping_cost = FloatField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'shipments',
        'indexes': ['tracking_number', 'sender', 'status']
    }

class Delivery(Document):
    """Delivery tracking model"""
    shipment = ReferenceField(Shipment, required=True)
    driver = ReferenceField(User)
    current_location = StringField()
    latitude = FloatField()
    longitude = FloatField()
    estimated_delivery_time = DateTimeField()
    actual_delivery_time = DateTimeField()
    delivery_notes = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'deliveries',
        'indexes': ['shipment', 'driver']
    }
