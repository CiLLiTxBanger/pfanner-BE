from rest_framework import serializers
from api.models import Season

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'scale', 'created_on', 'edited_on'] 