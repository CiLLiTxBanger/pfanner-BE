from rest_framework import serializers
from api.models import FrostSensitivity

class FrostSensitivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FrostSensitivity
        fields = ['id', 'scale', 'created_on', 'edited_on'] 