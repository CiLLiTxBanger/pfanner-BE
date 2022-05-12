from rest_framework import serializers
from api.models import FlavorMeasurement

class FlavorMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlavorMeasurement
        fields = ['id', 'scale', 'created_on', 'edited_on'] 