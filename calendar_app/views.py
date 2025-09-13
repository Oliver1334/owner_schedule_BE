from rest_framework import viewsets, generics
from .models import Event, EventException
from .serializers import EventSerializer, EventExceptionSerializer

# Event endpoints (full CRUD with one router)
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('start_time')
    serializer_class = EventSerializer

# EventException endpoints (leave as generics for now)
class EventExceptionListCreateView(generics.ListCreateAPIView):
    queryset = EventException.objects.all()
    serializer_class = EventExceptionSerializer

class EventExceptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventException.objects.all()
    serializer_class = EventExceptionSerializer