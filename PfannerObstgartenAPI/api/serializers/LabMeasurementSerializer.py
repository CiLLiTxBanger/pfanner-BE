from rest_framework import serializers
from api.models import LabMeasurement

class LabMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabMeasurement
        fields = ['id', 'timestamp', 'tree', 'strengthMeasurement', 'flavorMeasurement', 'acidMeasurement', 'sugarMeasurement', 'status', 'created_on', 'edited_on']

        def create(self, validated_data):
            return LabMeasurement.objects.create(**validated_data)