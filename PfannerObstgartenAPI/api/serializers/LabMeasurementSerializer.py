from rest_framework import serializers
from api.models import LabMeasurement
from api.serializers import TreeSerializer

class LabMeasurementSerializer(serializers.ModelSerializer):
    tree = TreeSerializer()

    class Meta:
        model = LabMeasurement
        fields = ['id', 'timestamp', 'tree', 'strengthMeasurement', 'flavorMeasurement', 'acidMeasurement', 'sugarMeasurement', 'status', 'created_on', 'edited_on']

class WriteLabMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabMeasurement
        fields = ['id', 'timestamp', 'tree', 'strengthMeasurement', 'flavorMeasurement', 'acidMeasurement', 'sugarMeasurement', 'status', 'created_on', 'edited_on']