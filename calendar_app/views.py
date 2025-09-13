from rest_framework import generics
from .models import Event, EventException
from .serializers import EventSerializer, EventExceptionSerializer

# Event endpoints
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# EventException endpoints
class EventExceptionListCreateView(generics.ListCreateAPIView):
    queryset = EventException.objects.all()
    serializer_class = EventExceptionSerializer

class EventExceptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventException.objects.all()
    serializer_class = EventExceptionSerializer