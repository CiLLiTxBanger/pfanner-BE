from rest_framework import serializers
from api.models import AcidMeasurement

class AcidMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcidMeasurement
        fields = ['id', 'scale', 'created_on', 'edited_on'] 