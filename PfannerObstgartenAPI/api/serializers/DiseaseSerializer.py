from rest_framework import serializers
from api.models import Disease

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['name', 'scale', 'created_on', 'edited_on'] 