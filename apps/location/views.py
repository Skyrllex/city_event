from rest_framework import viewsets, permissions
from .models import Location
from .serializers import LocationSerializer
#from django.shortcuts import render


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    premission_classes = [permissions.IsAdminUser]
