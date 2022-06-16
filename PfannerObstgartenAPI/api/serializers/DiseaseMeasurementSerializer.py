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