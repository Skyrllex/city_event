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
    return Event.objects.filter(status="published")

def get_premissions(self):
    if self.action in ['create','update','partial_update','destroy']:
        return [permissions.IsAdminUser()]
    return [permissions.IIsAuthenticatedOrReadOnly]

def get_serializer_context(self):
    context=super().get_serializer_context()
    context['request'] = self.request
    return context

def hello_world(request):
    return HttpResponse("<h1>HELLO WORLD!!!</h1>")

def event_list(request):
    #events = Event.objects.all()
    events = list(Event.objects.all())
    return render(request,'events/list.html', {'events': events})
    #events = Event.objects.all()
    #return render(request,'/events/templates/list.html', {'events': events})