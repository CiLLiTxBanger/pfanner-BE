from rest_framework import serializers
from api.models import OrchardMeasurement

class OrchardMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrchardMeasurement
        fields = ['description', 'tree', 'FrostSensitivity', 'growthHabit', 'yieldHabit', 'season', 'temperature', 'lateFrost', 'created_on', 'edited_on'] 