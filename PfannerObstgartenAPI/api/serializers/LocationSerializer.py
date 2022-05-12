from rest_framework import serializers
from api.models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'city', 'country', 'description', 'created_on', 'edited_on'] 