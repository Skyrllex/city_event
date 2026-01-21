from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'coordinateX', 'coordinateY','created_at', 'updates_at']