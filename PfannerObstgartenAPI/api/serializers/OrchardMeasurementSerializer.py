from rest_framework import serializers
from api.models import OrchardMeasurement

class OrchardMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrchardMeasurement
        fields = ['id', 'description', 'tree', 'image', 'frostSensitivity', 'growthHabit', 'yieldHabit', 'season', 'temperature', 'lateFrost', 'created_on', 'edited_on']
        depth = 1