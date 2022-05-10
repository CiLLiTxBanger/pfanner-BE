from rest_framework import serializers
from api.models import Temperature

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['scale', 'created_on', 'edited_on'] 