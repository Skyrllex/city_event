from rest_framework import viewsets, permissions
from .models import Event,Location
from .serializers import EventSerializer
from django.http import HttpResponse
from django.shortcuts import render
from .filters import EventFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.core.paginator import Paginator

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

    event_filter = EventFilter(request.GET, queryset=events)
    events_set= event_filter.qs

    paginator = Paginator (events_set,6)
    page_number=request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    return render(request,'events/list.html', {
        'events': page_obj,
        'filter': event_filter,
        'page_obj': page_obj,
        })

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_Class=EventFilter

   #search_fields = ['name','id_location__name']
    #ordering_fileds = ['name','start_date','end_date']
    #ordering=['-start_date']
