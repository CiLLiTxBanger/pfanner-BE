from rest_framework import serializers
from api.models import Tree
from api.serializers import *

class TreeAnalyticsSerializer(serializers.ModelSerializer):
    labMeasurement = LabMeasurementSerializer
    orchardMeasurement = OrchardMeasurementSerializer

    class Meta:
        model = Tree
        fields = ['labMeasurement', 'orchardMeasurement'] 