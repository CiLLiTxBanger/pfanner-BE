from rest_framework import serializers
from api.models import DiseaseMeasurement
from api.serializers import DiseaseSerializer

class DiseaseMeasurementSerializer(serializers.ModelSerializer):
    disease = DiseaseSerializer()

    class Meta:
        model = DiseaseMeasurement
        fields = ['id', 'value', 'orchardMeasurement', 'disease', 'created_on', 'edited_on'] 

class WriteDiseaseMeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiseaseMeasurement
        fields = ['id', 'value', 'orchardMeasurement', 'disease', 'created_on', 'edited_on']

    def create(self, validated_data):
        queryset = DiseaseMeasurement.objects.filter(orchardMeasurement=validated_data.get('orchardMeasurement'), disease=validated_data.get('disease'))
        if queryset.exists():
            queryset.delete()
        return super().create(validated_data)