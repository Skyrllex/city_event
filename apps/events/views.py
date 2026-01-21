from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer
#from django.shortcuts import render


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    premission_classes = [permissions.IsAdminUser]
