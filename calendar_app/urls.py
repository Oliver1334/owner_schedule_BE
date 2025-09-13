from django.urls import path
from .views import EventListCreateView, EventDetailView, EventExceptionListCreateView, EventExceptionDetailView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('exceptions/', EventExceptionListCreateView.as_view(), name='exception-list-create'),
    path('exceptions/<int:pk>/', EventExceptionDetailView.as_view(), name='exception-detail'),
]