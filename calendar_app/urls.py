from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventExceptionListCreateView, EventExceptionDetailView

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('exceptions/', EventExceptionListCreateView.as_view(), name='exception-list-create'),
    path('exceptions/<int:pk>/', EventExceptionDetailView.as_view(), name='exception-detail'),
]