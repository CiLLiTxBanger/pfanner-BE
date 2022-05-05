from rest_framework import serializers
from api.models import DiseaseMeasurement

class DiseaseMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseMeasurement
        fields = ['value', 'orchardMeasurement', 'disease', 'created_on', 'edited_on'] 