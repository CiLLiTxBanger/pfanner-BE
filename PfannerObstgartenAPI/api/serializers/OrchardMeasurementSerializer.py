from rest_framework import serializers
from api.models import OrchardMeasurement
from api.serializers import *

class OrchardMeasurementSerializer(serializers.ModelSerializer):
    tree = TreeSerializer()

    class Meta:
        model = OrchardMeasurement
        fields = ['id', 'description', 'tree', 'image_photo', 'image_description', 'frostSensitivity', 'growthHabit', 'yieldHabit', 'season', 'temperature', 'precipitation', 'lateFrost', 'status', 'created_on', 'edited_on', 'status']

class WriteOrchardMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrchardMeasurement
        fields = ['id', 'description', 'tree', 'image_photo', 'image_description', 'frostSensitivity', 'growthHabit', 'yieldHabit', 'season', 'temperature', 'precipitation', 'lateFrost', 'status', 'created_on', 'edited_on', 'status']
