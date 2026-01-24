from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet
from . import views

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('hello', views.hello_world, name='hello'),
    path('list', views.event_list, name='event_list'),
]