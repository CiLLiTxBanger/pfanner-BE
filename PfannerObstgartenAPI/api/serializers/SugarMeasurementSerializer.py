from rest_framework import serializers
from api.models import SugarMeasurement

class SugarMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SugarMeasurement
        fields = ['id', 'scale', 'created_on', 'edited_on'] 