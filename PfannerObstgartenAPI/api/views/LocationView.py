# under construction
from rest_framework import permissions
from api.models import Location
from api.serializers import LocationSerializer
from rest_framework import generics
from rest_framework import permissions
from django.core.exceptions import ValidationError

class LocationList(generics.ListAPIView):
    """
    List all Locations.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveAPIView):
    """
    Retrieve a Location.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

