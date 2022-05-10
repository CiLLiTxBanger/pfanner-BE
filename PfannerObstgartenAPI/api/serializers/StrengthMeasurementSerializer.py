from rest_framework import serializers
from api.models import StrengthMeasurement

class StrengthMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrengthMeasurement
        fields = ['scale', 'created_on', 'edited_on'] 