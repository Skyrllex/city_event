from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer
from django.http import HttpResponse
from django.shortcuts import render


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    premission_classes = [permissions.IsAdminUser]

def get_queryset(self):
    if self.request.user.is_superuser:
        return Event.objects.all()
    return Event.objects.filter(status="publication")

def get_premissions(self):
    if self.action in ['create','update','partial_update','destroy']:
        return [permissions.IsSuperUser()]
    return [permissions.IsAuthenticatedOrReadOnly]

def get_serializer_context(self):
    context=super().get_serializer_context()
    context['request'] = self.request
    return context

def hello_world(request):
    return HttpResponse("<h1>HELLO WORLD!!!</h1>")

def event_list(request):
    if request.user.is_superuser:
        events = Event.objects.all()
    else:
        events = Event.objects.filter(status = "publication")
    return render(request,'events/list.html', {'events': events})
