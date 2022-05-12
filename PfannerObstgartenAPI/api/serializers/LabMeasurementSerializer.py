from rest_framework import serializers
from api.models import LabMeasurement

class LabMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabMeasurement
        fields = ['id', 'timestamp', 'tree', 'strengthMeasurement', 'flavorMeasurement', 'acidMeasurement', 'sugarMeasurement', 'created_on', 'edited_on'] 