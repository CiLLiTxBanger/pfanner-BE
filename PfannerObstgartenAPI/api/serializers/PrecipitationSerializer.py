from rest_framework import serializers
from api.models import Precipitation

class PrecipitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precipitation
        fields = ['scale', 'created_on', 'edited_on'] 